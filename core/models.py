from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from core.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)

    def __str__(self):
        return 'Nome: {}'.format(self.name)

    def toJSON(self):
        item = {'id': self.id, 'name': self.name}
        model_to_dict
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nome')
    surnames = models.CharField(max_length=150, verbose_name='SobreNome')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Data de nascimento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Endereço')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

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


# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nome')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Typos'
#         ordering = ['id']
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nome')
#
#     def __str__(self):
#         # return self.name
#         return 'Nro: {} - Nome:{} '.format(self.id, self.name)
#
#     class Meta:
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'
#         ordering = ['id']
#
#
# # Create your models here.
# class Employee(models.Model):
#     category = models.ManyToManyField(Category)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     names = models.CharField(max_length=150, verbose_name='Nomes')
#     dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
#     date_joined = models.DateTimeField(default=datetime.now, verbose_name='Data do registro')
#     date_creation = models.DateTimeField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     age = models.PositiveIntegerField(default=0)
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     state = models.BooleanField(default=True)
#     # gender = models.CharField(max_length=50)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
#     cvitae = models.ImageField(upload_to='cvitae/%Y/%m/%d')
#
#     def __str__(self):
#         return self.names
#
#     class Meta:
#         verbose_name = 'Empregado'
#         verbose_name_plural = 'Empregados'
#         ordering = ['id']
