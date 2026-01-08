from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.select_related("categoria").prefetch_related("detalles")
    return render(request, "tienda/lista_productos.html", {"productos": productos})
