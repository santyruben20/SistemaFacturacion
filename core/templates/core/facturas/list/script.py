from django.shortcuts import redirect
from .....models import Factura

#eliminar usuarios
def eliminarFactura(_request, id):
    user=Factura.objects.get(id = id)
    user.delete();
    return redirect('/facturas-list/')
