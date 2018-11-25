# coding=utf-8

from .models import Categoria

def categorias(request):
    return {
        'categorias': Categoria.objects.all()
    }

