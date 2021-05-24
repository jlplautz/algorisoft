from django.urls import path
from core.views.category.views import CategoryUpdateView, CategoryDeleteView, \
    CategoryListView, CategoryCreateView, CategoryFormView
from core.views.dashboard.views import DashboardView

app_name = 'core'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
