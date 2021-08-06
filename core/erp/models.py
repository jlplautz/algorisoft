from crum import get_current_user
from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from core.models import BaseModel
from src.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
# from django.conf import settings


class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Description')

    def __str__(self):
        # return 'Nome: {}'.format(self.name)
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Category, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagem')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Preço d Venda')

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nome')
    surnames = models.CharField(max_length=150, verbose_name='SobreNome')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Data de nascimento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Endereço')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = self.get_gender_display()
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.names

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalhe de Venda'
        verbose_name_plural = 'Detalhe de Vendas'
        ordering = ['id']
