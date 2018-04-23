from django.shortcuts import render
from core.models import Produto
from core.models import Categoria

def index(request):
	contexto = {
		"produtos":Produto.objects.all()
	}
	return render(request, "index.html", contexto)		

def categorias(request):
	contexto = {
		"categorias":Categoria.objects.all()
	}
	return render(request, "index.html", contexto)	

# Create your views here.
