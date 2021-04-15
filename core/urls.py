from django.urls import path

from core.views import myfirstview, mysecondview

app_name = 'core'

urlpatterns = [
    path('first/', myfirstview, name='first'),
    path('second/', mysecondview, name='second')
]
