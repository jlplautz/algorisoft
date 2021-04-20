# cursoDjango3
Projeto baseado no site Algorisoft - Python com Django

## Como verificar a estrutura dos diretorio no projeto
  ### abrir o python console
  - >>> import os
  - >>> BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  - >>> BASE_DIR
      - '/home/plautz/PycharmProjects' 
        
  - >>> os.path.join(BASE_DIR, 'templates')

      - '/home/plautz/PycharmProjects/templates'

|[] (https://github.com/jlplautz/algorisoft/blob/main/asserts/images/dbase.png)


# Procedimento para implementar Datatable

## Apagar os registros da tabela com PostgreSQL
   - delete from erp_product; 
     - ALTER SEQUENCE erp_product_id_seq RESTART WITH 1; 
   - delete from erp_category;
     -ALTER SEQUENCE erp_category_id_seq RESTART WITH 1;

## Links de datatable
   - https://datatables.net/download/
   - https://datatables.net/examples/styling/bootstrap4
   - https://datatables.net/extensions/fixedheader/examples/styling/bootstrap4.html
   - https://datatables.net/examples/basic_init/language.html
   - http://cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json
   - https://datatables.net/examples/basic_init/zero_configuration.html

## Links para poder executar
    | <link rel="stylesheet" href="{% static 'lib/datatables-1.10.20/css/dataTables.bootstrap4.min.css' %}"/>
    | <link rel="stylesheet" href="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/css/responsive.bootstrap4.min.css' %}"/>
    | <script src="{% static 'lib/datatables-1.10.20/js/jquery.dataTables.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/js/dataTables.bootstrap4.min.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/js/dataTables.responsive.min.js' %}"></script>
    | <script src="{% static 'lib/datatables-1.10.20/plugins/responsive-2.2.3/js/responsive.bootstrap4.min.js' %}"></script>

## Propriedades para inserir ba DataTable
     $('#data').DataTable({
           responsive: true,
           autoWidth: false
      });

## Para trocar o idioma
    "language": {
       url : '{% static 'lib/datatables-1.10.20/spanish.txt' %}'
     }

# Metodo Dispatch
  - o metodo dispatch é um executado no inicio quando chamamos um modelo. 
  - O qual se encarrega de direcionar a execução para um GET ou POST dependendo da solicitação

## No exemplo vamos executar vamos sob-escrever o metodo
    def dispatch(self, request, *args, **kwargs):
        # caso o metodo usado seja um GET
        if request.method == 'GET':
            return redirect('core:category_list2')
        return super().dispatch(request, *args, **kwargs)
   
   - https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#django.views.generic.base.View.dispatch