from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from core.models import Category, Product


def myfirstview(request):
    # # para retornar um objeto HttpResponse
    # return HttpResponse('Hello World!')

    # # para retornar um objeto JsonResponse
    # data = {
    #     'name': 'Jorge Plautz'
    # }
    # return JsonResponse(data)

    # para renderizar saida com templates
    # neste caso os modulos urls.py conseguimos apresentar o template index.html
    # com programação no settings.py (templates) -> http://localhost:8000/prova/first/
    data = {
        'name': 'Jorge Plautz',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)


def mysecondview(request):
    data = {
        'name': 'Jorge Plautz',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
