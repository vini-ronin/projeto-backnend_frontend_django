from django.contrib import admin

from .models import Box, Categoria, CategoriaBox, Curso, Estudante, Recomendacao, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "concluida", "analise_sentimento", "score_polaridade")
    list_filter = ("concluida", "categoria", "analise_sentimento")
    search_fields = ("titulo", "descricao", "feedback_professor")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome", "descricao")


@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "cpf", "data_nascimento", "celular", "curso")
    list_filter = ("curso",)
    search_fields = ("nome", "email", "cpf", "celular")


@admin.register(CategoriaBox)
class CategoriaBoxAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome", "descricao")


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "feirante", "categoria", "tipo_produto", "ativo")
    list_filter = ("ativo", "categoria", "tipo_produto")
    search_fields = ("nome", "descricao", "localizacao", "tipo_produto")


@admin.register(Recomendacao)
class RecomendacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "box", "cliente", "cliente_nome", "analise_sentimento", "score_polaridade", "data_criacao")
    list_filter = ("analise_sentimento", "data_criacao")
    search_fields = ("texto_recomendacao", "cliente_nome", "cliente_email", "box__nome")
