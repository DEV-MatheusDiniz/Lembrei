from django import forms
from .models import Lembrete
CHOICES = [
    ('0', 'Pendente'),
    ('1', 'Concuido')
]

class FormLembrete(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = [
            'titulo',
            'descricao',
            'status'
        ]
        widgets={
            'titulo':forms.TextInput(attrs={
                'placeholder':'Titulo',
                'id':'exampleInputText1',
                'class':'form-control'
            }),
            'descricao':forms.TextInput(attrs={
                'placeholder':'Descrição',
                'id':'exampleInputText2',
                'class':'form-control'
            }),
            'status':forms.Select(
                choices=CHOICES,
                attrs={
                'id':'exampleSelect1',
                'class':'form-control'
            })
        }
