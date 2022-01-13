from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import render
from .models import Producto, CategoriaProducto


# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()
    paginador = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginador.get_page(page_number)

    context = {'productos':productos, 
               'categorias':categorias,
               'productos':page_obj,

    }
    return render(request, 'tienda/tienda.html', context)


def categoria(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    return render(request, 'tienda/categoria.html', {'productos':productos,'categoria':categoria,})