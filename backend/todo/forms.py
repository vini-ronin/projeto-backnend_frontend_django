from django import forms
from .models import Categoria,Tarefa

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control',
             'placeholder':'Ex: Java, Python, Cloud, IA, Ciência de Dados',
             'style':'max-width:370px;'               
            })
        }


class TarefaForm(forms.ModelForm):
      # Adicione este bloco para injetar o texto no select do banco de dados
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'categoria' in self.fields:
            self.fields['categoria'].empty_label = "Escolha a categoria"
    class Meta:
            model = Tarefa
            fields = ['titulo', 'descricao', 'categoria','feedback_professor']
            widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da Tarefa'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição detalhada da tarefa'}),
            # Aqui está a mágica: adicionamos as escolhas com o placeholder desejado
            'categoria': forms.Select(
                attrs={'class': 'form-control form-select'}
            ),
            'feedback_professor': forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': 'Feedback do Professor'}), }


  