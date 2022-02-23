from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Здесь будет пост {slug}, если тебе не надоест программировать.')