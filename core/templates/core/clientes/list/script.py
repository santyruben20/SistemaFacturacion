from django.shortcuts import redirect
from .....models import Cliente

#eliminar usuarios
def eliminarCliente(_request, id):
    user=Cliente.objects.get(id = id)
    user.delete();
    return redirect('/clientes-list/')
