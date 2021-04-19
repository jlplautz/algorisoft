from django.urls import path

from core.views.category.views import CategoryListView

app_name = 'core'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list')
]
