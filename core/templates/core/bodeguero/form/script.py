from django.shortcuts import redirect
from .....models import Bodeguero

#registro de bodeguero
def registroBodeguero(request):
    bodegueros = Bodeguero(nombres = request.POST['nombres'], apellidos = request.POST['apellidos'], direccion = request.POST['direccion'], 
    telefono = request.POST['telefono'], tipo_de_licencia = request.POST['tipo_de_licencia'],  email = request.POST['email'], 
    clave = request.POST['clave'])
    bodegueros.save()
    return redirect('/bodegueros-list')

def eliminarBodeguero(_request, id):
    user = Bodeguero.objects.get(id = id)
    user.delete();
    return redirect('/bodegueros-list')