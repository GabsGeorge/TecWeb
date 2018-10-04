from django.shortcuts import render, get_object_or_404
from catalogo.models import Categoria
from catalogo.models import Produto
from django.views import generic
from django.db import models
# Create your views here.

#Categorias
class CategoriaListView(generic.ListView):
    template_name = 'catalogo/categoria.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.filter(categoria_p__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context    
    paginate_by = 9

categoria = CategoriaListView.as_view() 



#Listatgem de produtos
class ListProdutoView(generic.ListView):
    model = Produto
    template_name = 'catalogo/lista_produto.html'
    context_object_name = 'produtos'
    paginate_by = 9

    def get_queryset(self):
        queryset = Produto.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(nome_p__icontains=q) | models.Q(categoria_p__nome__icontains=q) \
                | models.Q(descricao__icontains=q)
            )
        return queryset

lista_produto = ListProdutoView.as_view()


#Produto unico
def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto_atual': produto,
    }
    return render(request, 'catalogo/produto_unico.html', contexto)      