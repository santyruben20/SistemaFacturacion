from django.shortcuts import redirect
from .....models import UsuarioAdministrador

#eliminar usuarios
def eliminarUsuario(_request, id):
    user=UsuarioAdministrador.objects.get(id = id)
    user.delete();
    return redirect('/usuarios-list/')
