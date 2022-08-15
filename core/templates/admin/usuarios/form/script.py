from django.shortcuts import redirect
from .....models import UsuarioAdministrador

#registrar usuarios
def registroUsuario(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']
    clave = request.POST['clave']

    Usuario = UsuarioAdministrador.objects.create( nombres = nombres, apellidos = apellidos, direccion = direccion,
      telefono = telefono, email = email, clave = clave)
    return redirect('/')