from django.shortcuts import redirect
from .....models import Cajero

#eliminar usuarios
def eliminarCajero(_request, id):
    user=Cajero.objects.get(id = id)
    user.delete();
    return redirect('/cajeros-list/')
