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
    return render(request, "catalogo/lista_produto.html")

def produto(request): #, slug):
    #contexto = {
    #    'produto': get_object_or_404(Produto, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    #}
    template_name = 'produto.html'
    return render(request, template_name)      