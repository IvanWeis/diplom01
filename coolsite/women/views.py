from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return HttpResponse('Страница приложения women')

def categories(request, catid): # из urls получает catid
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')
