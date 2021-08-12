from datetime import datetime

from django.forms import ModelForm, Form, Textarea, TextInput, ModelChoiceField, Select, DateInput, CharField
from core.erp.models import Category, Product, Client


class CategoryForm(ModelForm):
    # metodo __init__ para inicialisar o form e evitar duplicidade de codigo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.widget.attrs['class'] = 'form-control'
    #         form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
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
        # para excluir bo formularios os campos
        exclude = ['user_updated', 'user_creation']

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


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Inserir um nome',
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


class TestForm(Form):
    categorias = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control'
    }))

    # como deve estar vazio fazemos a queryset com objects.none()
    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Inserir uma descrição'
    }))


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Inserir seu nome',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Inserir seu sobrenome',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Inserir seu RG',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d', attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Inserir seu endereço',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
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
