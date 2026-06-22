from rest_framework import serializers

from .models import Box, CategoriaBox, Curso, Estudante, Recomendacao


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ["id", "nome", "email", "cpf", "data_nascimento", "celular"]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class CategoriaBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaBox
        fields = "__all__"


class BoxSerializer(serializers.ModelSerializer):
    total_recomendacoes = serializers.IntegerField(read_only=True)
    media_polaridade = serializers.FloatField(read_only=True)

    class Meta:
        model = Box
        fields = "__all__"
        read_only_fields = ("feirante", "data_criacao", "data_atualizacao")


class RecomendacaoSerializer(serializers.ModelSerializer):
    box_nome = serializers.CharField(source="box.nome", read_only=True)
    cliente_username = serializers.CharField(source="cliente.username", read_only=True)

    class Meta:
        model = Recomendacao
        fields = "__all__"
        read_only_fields = (
            "analise_sentimento",
            "score_polaridade",
            "data_criacao",
            "cliente",
        )
