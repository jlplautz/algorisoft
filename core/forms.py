from django.forms import ModelForm, TextInput, Textarea
# from django.db import models
from core.models import Category


class CategoryForm(ModelForm):
    # metodo __init__ para inicialisar o form e evitar duplicidade de codigo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.widget.attrs['class'] = 'form-control'
    #         form.field.widget.attrs['autocomplete'] = 'off'
    #         # para colocar foco no TextInput
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'name', 'desc']
        labels = {
            'name': 'Nome',
            'desc': 'Descrição'
        }
        # Propriedade para personalizar os componentes ou mesmo sob-escreve-los
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Inserir um nome'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Inserir um nome',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    # sobre-escrita do processo save
    def save(self, commit=True):
        # criar um variavel
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Mensagem de error')
    #         # self.add_error('name', 'Caracteres insuficentes')
    #     return cleaned
