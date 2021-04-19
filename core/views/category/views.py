from django.shortcuts import render
from django.views.generic import ListView

from core.models import Category


# listar Categorias com Function View
def category_list(request):
    data = {
        'title': 'Lista de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


# listar Categorias com Classe Base View - desde Django 1.3 temos -> Generic List
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # Sob-escrever o metodo queryset para model Category
    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='L')

    # Para sob-escrever o metodo -> get_context_data para alterar dados no context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Categorias'
        # um exemplo usando o model Product
        # context['object_list'] = Product.objects.all()
        return context
