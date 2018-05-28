from django.shortcuts import render
from catalogo.models import Categoria
# Create your views here.


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)  
    contexto = {
        'categoria': categoria, 
        'produtos': Produto.objects.filter(categoria=categoria),
       
    }
    return render(request,'categoria.html', contexto) 


def lista_produto(request):
    pass

def produto(request): #, slug):
    #contexto = {
    #    'produto': get_object_or_404(Produto, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    #}
    template_name = 'produto.html'
    return render(request, template_name)      