from django.urls import path

from core.views.category.views import CategoryUpdateView, CategoryDeleteView, \
    CategoryListView, CategoryCreateView, category_list

app_name = 'core'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
    # redirecionar usando dispatch na view
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete')
]
