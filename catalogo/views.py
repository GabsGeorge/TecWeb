from django.shortcuts import render
from catalogo.models import Categoria
from catalogo.models import Produto
from django.views import generic
# Create your views here.

class CategoriaListViwe(generic.ListView):
    template_name = 'catalogo/categoria.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(categoria__slug=self.kwargs['slug'])

categoria = CategoriaListViwe.as_Viwe()


def lista_produto(request):
    contexto = {
        'produtos':Produto.objects.all(),
        'categorias':Categoria.objects.all()
    }
    return render(request, "catalogo/lista_produto.html", contexto)


def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto_atual': produto,
        'categorias':Categoria.objects.all()
    }
    return render(request, 'catalogo/produto.html', contexto)      