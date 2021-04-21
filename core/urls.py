from django.urls import path

from core.views.category.views import CategoryListView, category_list, CategoryCreateView

app_name = 'core'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
    # redirecionar usando dispatch na view
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create')
]
