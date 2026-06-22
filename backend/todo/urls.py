from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BoxViewSet,
    CategoriaBoxViewSet,
    CursoViewSet,
    EstatisticasBoxesViewSet,
    EstudanteViewSet,
    RecomendacaoViewSet,
    listar_tarefas,
    nova_categoria,
    nova_tarefa,
)

router = DefaultRouter()
router.trailing_slash = "/?"
router.register(r"categorias-box", CategoriaBoxViewSet, basename="categoria-box")
router.register(r"estudantes", EstudanteViewSet, basename="estudante")
router.register(r"cursos", CursoViewSet, basename="curso")
router.register(r"boxes", BoxViewSet, basename="box")
router.register(r"recomendacoes", RecomendacaoViewSet, basename="recomendacao")
router.register(r"estatisticas/boxes", EstatisticasBoxesViewSet, basename="estatisticas-boxes")

urlpatterns = [
    path("categoria/", nova_categoria, name="categoria"),
    path("tarefa/", nova_tarefa, name="nova_tarefa"),
    path("listar_tarefas/", listar_tarefas, name="listar_tarefas"),
    path("api/", include(router.urls)),
]
