from django.conf import settings
from django.db import models

# tabela de categoria
# tabela de tarefas

class Categoria(models.Model):
    nome = models.CharField(max_length=100,
                             verbose_name="Nome da Categoria")
    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    # dados da tarefa
    titulo = models.CharField(max_length=200,verbose_name="Titulo da Tarefa",blank=True,null=True)
    descricao = models.TextField(verbose_name="Descriçaõ da Tarefa",blank=True,null=True)
    concluida = models.BooleanField(default=False,verbose_name="Concluída")
    # relacionamento 1:NOTE - 
    # SET_NULL ele apaga o vínculo e apenas isso. Ele deixa o campo da categoria das tarefas "vazio";
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Categoria")

    # dados da PLN (processamento de linguagem natural)
    # IA para análise de sentimentos

    feedback_professor = models.TextField(verbose_name="Feedback Professor",blank=True,null=True)
    analise_sentimento = models.CharField(max_length=50,verbose_name="Análise de Sentimento",blank=True,null=True)
    score_polaridade = models.FloatField(default=0.0,verbose_name="Score de Polaridade")

    def __str__(self):
        return f"{self.titulo or 'Sem titulo'} - {self.score_polaridade}"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")

    class Meta:
        ordering = ["nome"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome


class Estudante(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    celular = models.CharField(max_length=20, verbose_name="Celular")
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        related_name="estudantes",
        blank=True,
        null=True,
        verbose_name="Curso",
    )

    class Meta:
        ordering = ["nome"]
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

    def __str__(self):
        return self.nome


class CategoriaBox(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria de Box"
        verbose_name_plural = "Categorias de Boxes"

    def __str__(self):
        return self.nome


class Box(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Box")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")
    localizacao = models.CharField(max_length=255, verbose_name="Localizacao")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    feirante = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="boxes",
        verbose_name="Feirante",
    )
    categoria = models.ForeignKey(
        CategoriaBox,
        on_delete=models.SET_NULL,
        related_name="boxes",
        blank=True,
        null=True,
        verbose_name="Categoria",
    )
    horario_funcionamento = models.CharField(max_length=120, blank=True, null=True)
    tipo_produto = models.CharField(max_length=120, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Box"
        verbose_name_plural = "Boxes"

    def __str__(self):
        return self.nome


class Recomendacao(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="recomendacoes")
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="recomendacoes",
        blank=True,
        null=True,
    )
    cliente_nome = models.CharField(max_length=120, blank=True, null=True)
    cliente_email = models.EmailField(blank=True, null=True)
    texto_recomendacao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    analise_sentimento = models.CharField(max_length=80, blank=True, null=True)
    score_polaridade = models.FloatField(default=0.0)

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Recomendacao"
        verbose_name_plural = "Recomendacoes"

    def __str__(self):
        cliente = self.cliente.username if self.cliente else self.cliente_nome or "Anonimo"
        return f"Recomendacao para {self.box.nome} por {cliente}"
  


