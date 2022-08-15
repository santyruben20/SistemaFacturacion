from django.shortcuts import redirect
from .....models import Categoria

#eliminar usuarios
def eliminarCategoria(_request, id):
    user=Categoria.objects.get(id = id)
    user.delete();
    return redirect('/categorias-list/')
