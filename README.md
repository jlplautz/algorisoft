# cursoDjango3
Projeto baseado no site Algorisoft - Python com Django

##  Como verificar a estrutura dos diretorio no projeto
  - abrir o python console
  - >>> import os
  - >>> BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  - >>> BASE_DIR
      - '/home/plautz/PycharmProjects' 
        
  - >>> os.path.join(BASE_DIR, 'templates')

      - '/home/plautz/PycharmProjects/templates'

|[] (https://github.com/jlplautz/algorisoft/blob/main/asserts/images/dbase.png)


## Procedimento para implementar Datatable

###  Apagar os registros da tabela com PostgreSQL
   - delete from erp_product; 
     - ALTER SEQUENCE erp_product_id_seq RESTART WITH 1; 
   - delete from erp_category;
     -ALTER SEQUENCE erp_category_id_seq RESTART WITH 1;

###  Links de datatable
   - https://datatables.net/download/
   - https://datatables.net/examples/styling/bootstrap4
   - https://datatables.net/extensions/fixedheader/examples/styling/bootstrap4.html
   - https://datatables.net/examples/basic_init/language.html
   - http://cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json
   - https://datatables.net/examples/basic_init/zero_configuration.html

###  Links para poder executar
    | <link rel="stylesheet" href="{% static 'lib/datatables-1.10.20/css/dataTables.bootstrap4.min.css' %}"/>
    | <link rel="stylesheet" href="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/css/responsive.bootstrap4.min.css' %}"/>
    | <script src="{% static 'lib/datatables-1.10.20/js/jquery.dataTables.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/js/dataTables.bootstrap4.min.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/js/dataTables.responsive.min.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/js/responsive.bootstrap4.min.js' %}"></script>

###  Propriedades para inserir ba DataTable
     $('#data').DataTable({
           responsive: true,
           autoWidth: false
      });

###  Para trocar o idioma
    "language": {
       url : '{% static 'lib/datatables-1.10.20/spanish.txt' %}'
     }

# Método Dispatch
  - o metodo dispatch é um executado no inicio quando chamamos um modelo. 
  - O qual se encarrega de direcionar a execução para um GET ou POST dependendo da solicitação

###  No exemplo vamos executar vamos sob-escrever o metodo
    def dispatch(self, request, *args, **kwargs):
        # caso o metodo usado seja um GET
        if request.method == 'GET':
            return redirect('core:category_list2')
        return super().dispatch(request, *args, **kwargs)
   
   - https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#django.views.generic.base.View.dispatch

## Decorator
  - Decoradores -> são funçoes que agregam funcionalidades em outras funçoes.
  - Os decoradores permitem alterar de maneira dinamica a funcionalidade de uma função
  - necessário usar django.utils.decorators import method_decorator

### Neste exemplo vamos usar um decorator para validar se usuario ewsta logado
    @login_required()
    def dispatch(self, request, *args, **kwargs):
        # caso o metodo usado seja um GET
        # if request.method == 'GET':
        #     return redirect('core:category_list2')
        return super().dispatch(request, *args, **kwargs)


## Metodo POST
  - método Post tem a mesma parametrização do metodo Dispatch
  - quando ocorre uma solicitação com metodo Post - que envolve um objeto (retorna um dicionário)
  
  def post(self, request, *args, **kwargs):
      data = {'nome': 'Jorge Plautz'}
      return JsonResponse(data)
  
### Executando via Postman verificamos que ocorre erro CSRF  
    - Forbidden (CSRF cookie not set.): /core/category/list
    
### Django tem um mecânico ativo para proteger aplicação com relação ao método POST 
   - no file Settings.pt -> sessão MIDDLEWARE
   - 'django.middleware.csrf.CsrfViewMiddleware'
   - Comentado esta linha tiramos esta proteção

### Podemos usar o decorator para desativar a proteção
   -@csrf_exempt()

## Como usar Ajax com método Post
  - Ajax é uma tecnologia do tipo async. Permitindo desta forma recarregar somente algumas 
    informações da pagina. Não necessariamente toda a pagina
    
### No botão de inserir uma Categoria nova foi inserido o evento para Ajax Video 25
  <button class="btn btn-primary btn-flat btnTest"></button> 
  - inserir um alert para verificar se esta funcionando
    - $('.btnTest').on('click', function() { alert(x) });

  - inserir a função Ajax -> templates/list.html no botão "Novo Registro"
    
            $('.btnTest').on('click', function() {
                $.ajax({
                    url: '{% url 'core:category_list' %}', type: 'POST', data: {id: 1},
                    DataType: 'json'
                }).done(function (data) {
                    console.log(data);
                }).fail(function(jqXHR, textStatus, errorThrown){
                    alert(textStatus+ ':' +errorThrown );
                }).always(function(data) {
                    alert("complete");
                });
            });
    
 - inserir no models.py
   
        def toJSON(self):
        item = {'id': self.id, 'name': self.name}
        return item
      
  - Test para verificar model_to_dict
    - (.venv) algorisoft $ mng shell
      - from django.forms import model_to_dict
      - from core.models import Category
      - cat = Category
      - cat = Category.objects.first()
      - model_to_dict(cat)
      - 'id': 1, 'name': 'Leche y derivados'}
    
## Criar o primeiro formulário Video 26
  - criar um file forms.py dentro da app core
  - link -> https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
### criar um file file forms.py e uma class CategoryForm 

      class CategoryForm(ModelForm):
         class Meta:
            model = Category
            fields = '__all__'
            template_name = 'category/create.html'
    
### criar uma class views/category/view.py

    class CategoryCreateView(CreateView):
        model = Category
        form_class = CategoryForm
        template_name = 'category/create.html'
        # Redirecionar quando salvar
        success_url = reverse_lazy('core:category_list')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Criar Categoria'
            return context

### criar um template core/templates/category/create.html

    {% extends 'body.html' %}
    {% block content %}
        <form method="post" action=".">
            <div class="card card-default">
            <div class="card-header">
                <h3 class="card-title">
                   <i class="fas fa-plus"></i>
                   {{ title }}
               </h3>
            </div>
            <div class="card-body">
                {% csrf_token %}
                {# Para renderizar o componente form #}
                {{ form.as_p }}
            </div>
            <div class="card-footer">
                <button type="submit" class="btn btn-primary btn-flat">
                 <i class="fas fa-save"></i> Salvar Registro
                </button>
         </div>
        </div>
        </form>
    {% endblock %}

### criar URL 
    path('category/add/', CategoryCreateView.as_view(), name='category_create')


## Personalizar o primeiro formulário Video 27

### inicializar o form -> core/forms.py
   
    # metodo __init__ para inicialisar o form e evitar duplicidade de codigo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            # para colocar foco no TextInput
            self.fields['name'].widget.attrs['autofocus'] = True

### implementação para renderizar o template -> templates/category/create.html
  
    {# Para renderizar o componente form #}
        {% for field in form.visible_fields %}
            <div class="form-group">
                 <label for="email">{{ field.label }}:</label>
                      {{ field }}
            </div>

### Instalar a lib django-widget-tweaks 
   - pip install django-widget-tweaks 
   - INSTALLED_APPS -> 'widget_tweaks'
   - inserir dentro do template -> {% load widget_tweaks %}
     
   - com a instalação da lib 'widget_tweaks' todemos remover a implementação do formulário
   - link -> https://github.com/jazzband/django-widget-tweaks

    #     for form in self.visible_fields():
    #         form.field.widget.attrs['class'] = 'form-control'
    #         form.field.widget.attrs['autocomplete'] = 'off'
    #         # para colocar foco no TextInput

   - mas tem que alterar template -> templates/category/create.html
    
    {# Para renderizar o componente form #}
         {% for field in form.visible_fields %}
            <div class="form-group">
               <label for="email">{{ field.label }}:</label>
                  {{ field|add_class:'form-control'|attr:'autocompĺete:off' }}
            </div>
         {% endfor %}

## Validar o primeiro formulário Video 28

### Para sinalizar erro quando o formulário for preenchido
   - core/templates/category/create.html
    <div class="card-body">
        {% csrf_token %}
        {# Sinalizar possivel erro qdo o formulário for preenchido  #}
        {{ form.errors }}

### No views/templates/views podemos sob-escrever o metodo POST

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

### Podemos tambem comentar o codigo da views/templates/views
   - core/templates/category/create.html
     

    {# Sinalizar possivel erro qdo o formulário for preenchido  #}
    {% if form.errors %}
       <div class="alert alert-warning alert-dismissible">
           <button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>
           <h5><i class="icon fa fa-ban"></i> Ocorreu um erro ao salvar o registro</h5>
           <ul>
               {% for field in form %}
                   {% for error in field.errors %}
                       <li>{{ error }}</li>
                   {% endfor %}
               {% endfor %}
           </ul>
       </div>
    {% endif %}

### Podemos ter outra possibilidade da views/templates/views
   - instalar os recursos da lib sweetalert2 no static/lib
     - https://sweetalert2.github.io/#download
     - /home/plautz/PycharmProjects/algorisoft/static/lib/sweetalert2-9.10.0/
       
   - inserir no template home
     
    <!-- sweetalert2 -->
    <script src="{% static 'lib/sweetalert2-9.10.0/sweetalert2.all.min.js' %}"></script>

   - core/templates/category/create.html

    <script>
        {% if form.errors %}
            var errors = '';
            {% for field in form %}
                {% for error in field.errors %}
                    errors+= '{{ error }}\n';
                {% endfor %}
            {% endfor %}
        {% endif %}
        Swal.fire({
            title: 'Error!',
            text: errors,
            icon: 'error',
        });

### Criar link da pagina de LISTAR Categorias para Salvar novo registro
   -  na pagina templates/list.html
      
    <a href="{{ create_url }}" class="btn btn-primary btn-flat btnTest">
       <i class="fas fa-plus"></i> Novo Registro
    </a>

   -  na views/category/views na função get_context_data(self, **kwargs)
      - criar a rota 

    def get_context_data(self, **kwargs):
        . . . 
        # create_url -> para encaminhar da list -> create category
        context['create_url'] = reverse_lazy('core:category_create')

### Criar link da pagina de LISTAR Categorias - entity para Categorias
   -  na pagina templates/body.html

    <li class="breadcrumb-item"><a href="#">Layout</a></li>
    <!-- alterar para --> 
    <li class="breadcrumb-item"><a href="{{ list_url }}">{{ entity }}</a></li>
    
   - na view -> class CategoryListView(ListView):

    def get_context_data(self, **kwargs):
        . . . 
        context['create_url'] = reverse_lazy('core:category_create')
        context['list_url'] = reverse_lazy('core:category_list')
        context['entity'] = 'Categorias'
    
   - na view -> class CategoryCreateView(CreateView):

    def get_context_data(self, **kwargs):
        . . . 
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('core:category_list')


## Implementar AJAX para enviar os dados Video 29
  - Implementar AJAX com view generic (CBV)
  - No file templates/form.html inserir no block content:
  
        $('form').on('submit', function(e) {
            e.preventDefault();
            // criar um variavel para obter todos os dados do formulário
            // e atraves de uma jquery podemos enviar todos os dados da
            var parameters = $(this).serializeArray();
            $.ajax({
                    url: '{% url 'core:category_create' %}',
                    type: 'POST',
                    data: {id: 1},
                    DataType: 'json'
                }).done(function (data) {
                    console.log(data);
                }).fail(function(jqXHR, textStatus, errorThrown){
                    alert(textStatus+':'+errorThrown );
                }).always(function(data) {
                    alert("complete");
                });
        });

  - inserir um action no get_context_data -> class CategoryCreateView(CreateView)
    - context['action'] = 'add'
    
  - inserir no templates/forms um input 
    -  <input type="hidden" name="action" value="{{ action }}">
    
  - Alterar o metodo POST -> class CategoryCreateView(CreateView):   

Parei o video com 13:17