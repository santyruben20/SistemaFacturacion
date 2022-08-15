from django.shortcuts import redirect
from .....models import Cajero

def registroCajero(request):
    cajero = Cajero(
        nombres = request.POST['nombres'],
        apellidos = request.POST['apellidos'],
        direccion = request.POST['direccion'],
        telefono = request.POST['telefono'],
        exp_laboral = request.POST['exp_laboral'],
        idiomas = request.POST['idiomas'],
        email = request.POST['email'],
        clave = request.POST['clave'],
    )
    cajero.save()
    return redirect('/cajeros-list')
