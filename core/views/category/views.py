# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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

    # @login_required()
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        # caso o metodo usado seja um GET
        # if request.method == 'GET':
        #     return redirect('core:category_list2')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

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
