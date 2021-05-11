# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.models import Category
from core.forms import CategoryForm


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
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ocorreu um error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # Sob-escrever o metodo queryset para model Category
    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='L')

    # Para sob-escrever o metodo -> get_context_data para alterar dados no context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Categorias'
        # create_url -> para encaminhar da list -> create category
        context['create_url'] = reverse_lazy('core:category_create')
        context['list_url'] = reverse_lazy('core:category_list')
        context['entity'] = 'Categorias'

        # um exemplo usando o model Product
        # context['object_list'] = Product.objects.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    # Redirecionar quando salvar
    success_url = reverse_lazy('core:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No foi selecionada nenhuma opção!!!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # # validar campos do formulário
    # def post(self, request, *args, **kwargs):
    #     form = CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('core:category_list')
        context['action'] = 'add'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('core:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No foi selecionada nenhuma opção!!!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('core:category_list')
        context['action'] = 'edit'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('core:category_list')

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deletar Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('core:category_list')
        return context
