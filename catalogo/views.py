from django.shortcuts import render
from catalogo.models import Categoria
from catalogo.models import Produto
# Create your views here.


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)  
    contexto = {
        'categoria_atual': categoria, 
        'produtos': Produto.objects.filter(categoria_p=categoria),   
    }
    return render(request,'catalogo/categoria.html', contexto) 

def lista_produto(request):
    contexto = {
        "produtos":Produto.objects.all()
    }
    return render(request, "catalogo/lista_produto.html", contexto)


def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto_atual': produto,
    }
    return render(request, 'catalogo/produto.html', contexto)      