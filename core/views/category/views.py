from django.shortcuts import render

from core.models import Category


def category_list(request):
    data = {
        'title': 'Lista de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)
