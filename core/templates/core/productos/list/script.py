from django.shortcuts import redirect
from .....models import Factura, Producto

#eliminar usuarios
def eliminarProducto(_request, id):
    user=Producto.objects.get(id = id)
    user.delete();
    return redirect('/productos-list/')
