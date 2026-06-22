from django.db.models import Avg, Count, Q
from django.shortcuts import redirect, render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .forms import CategoriaForm, TarefaForm
from .models import Box, CategoriaBox, Curso, Estudante, Recomendacao, Tarefa
from .serializers import (
    BoxSerializer,
    CategoriaBoxSerializer,
    CursoSerializer,
    EstudanteSerializer,
    RecomendacaoSerializer,
)
from .utils import executar_nlp_raiz


def nova_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_tarefas")
    else:
        form = CategoriaForm()
    return render(request, "todo/nova_categoria.html", {"form": form})


def nova_tarefa(request):
    form = TarefaForm()
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            sentimento, score = executar_nlp_raiz(tarefa.feedback_professor)
            tarefa.analise_sentimento = sentimento
            tarefa.score_polaridade = score
            tarefa.save()
            return redirect("listar_tarefas")
    return render(request, "todo/nova_tarefa.html", {"form": form})


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "todo/listar_tarefas.html", {"tarefas": tarefas})


class CategoriaBoxViewSet(viewsets.ModelViewSet):
    queryset = CategoriaBox.objects.all()
    serializer_class = CategoriaBoxSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [AllowAny]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [AllowAny]


class BoxViewSet(viewsets.ModelViewSet):
    serializer_class = BoxSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Box.objects.select_related("feirante", "categoria").annotate(
            total_recomendacoes=Count("recomendacoes"),
            media_polaridade=Avg("recomendacoes__score_polaridade"),
        )
        tipo_produto = self.request.query_params.get("tipo_produto")
        categoria = self.request.query_params.get("categoria")
        ativo = self.request.query_params.get("ativo")

        if tipo_produto:
            queryset = queryset.filter(tipo_produto__icontains=tipo_produto)
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        if ativo is not None:
            queryset = queryset.filter(ativo=ativo.lower() in ["1", "true", "sim"])

        return queryset

    def perform_create(self, serializer):
        serializer.save(feirante=self.request.user)

    @action(detail=True, methods=["get"], permission_classes=[AllowAny])
    def estatisticas(self, request, pk=None):
        box = self.get_object()
        recomendacoes = box.recomendacoes.all()
        sentimentos = recomendacoes.values("analise_sentimento").annotate(total=Count("id"))

        return Response(
            {
                "box": box.nome,
                "total_recomendacoes": recomendacoes.count(),
                "media_polaridade": recomendacoes.aggregate(media=Avg("score_polaridade"))["media"] or 0,
                "positivas": recomendacoes.filter(score_polaridade__gt=0.1).count(),
                "neutras": recomendacoes.filter(score_polaridade__gte=-0.1, score_polaridade__lte=0.1).count(),
                "negativas": recomendacoes.filter(score_polaridade__lt=-0.1).count(),
                "distribuicao_sentimentos": list(sentimentos),
            }
        )


class RecomendacaoViewSet(viewsets.ModelViewSet):
    serializer_class = RecomendacaoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Recomendacao.objects.select_related("box", "cliente")
        box = self.request.query_params.get("box")
        sentimento = self.request.query_params.get("sentimento")

        if box:
            queryset = queryset.filter(box_id=box)
        if sentimento:
            queryset = queryset.filter(analise_sentimento__icontains=sentimento)

        return queryset

    def perform_create(self, serializer):
        texto = serializer.validated_data.get("texto_recomendacao", "")
        sentimento, polaridade = executar_nlp_raiz(texto)
        cliente = self.request.user if self.request.user.is_authenticated else None
        serializer.save(
            cliente=cliente,
            analise_sentimento=sentimento,
            score_polaridade=polaridade,
        )


class EstatisticasBoxesViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        recomendacoes = Recomendacao.objects.all()
        boxes = Box.objects.annotate(
            total_recomendacoes=Count("recomendacoes"),
            media_polaridade=Avg("recomendacoes__score_polaridade"),
            positivas=Count("recomendacoes", filter=Q(recomendacoes__score_polaridade__gt=0.1)),
            neutras=Count(
                "recomendacoes",
                filter=Q(
                    recomendacoes__score_polaridade__gte=-0.1,
                    recomendacoes__score_polaridade__lte=0.1,
                ),
            ),
            negativas=Count("recomendacoes", filter=Q(recomendacoes__score_polaridade__lt=-0.1)),
        )

        ranking = [
            {
                "id": box.id,
                "nome": box.nome,
                "total_recomendacoes": box.total_recomendacoes,
                "media_polaridade": box.media_polaridade or 0,
                "positivas": box.positivas,
                "neutras": box.neutras,
                "negativas": box.negativas,
            }
            for box in boxes.order_by("-media_polaridade", "-total_recomendacoes")
        ]

        return Response(
            {
                "total_boxes": Box.objects.count(),
                "total_recomendacoes": recomendacoes.count(),
                "media_geral_polaridade": recomendacoes.aggregate(media=Avg("score_polaridade"))["media"] or 0,
                "distribuicao_sentimentos": list(
                    recomendacoes.values("analise_sentimento").annotate(total=Count("id"))
                ),
                "ranking_boxes": ranking,
            },
            status=status.HTTP_200_OK,
        )
