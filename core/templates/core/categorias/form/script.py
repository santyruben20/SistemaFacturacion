from django.shortcuts import redirect
from .....models import Categoria, Producto

def registroCategoria(request):
    categoria = Categoria(
        descripcion = request.POST['descripcion'],
        bodeguero = request.POST['bodeguero'],
    )
    categoria.save()
    return redirect('/categorias-list')

def eliminarCategoria(_request, id):
    categoria = Categoria.objects.get(id = id)
    categoria.delete();
    return redirect('/categorias-list')