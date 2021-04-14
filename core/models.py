from django.db import models
from datetime import datetime


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Typos'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


# Create your models here.
class Employee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nomes')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Data do registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    # gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    cvitae = models.ImageField(upload_to='cvitae/%Y/%m/%d')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['id']
