from django.shortcuts import redirect
from .....models import Cliente

def registroCliente(request):
    cliente= Cliente(
        cedula = request.POST['cedula'], 
        nombres = request.POST['nombres'], 
        apellidos = request.POST['apellidos'], 
        direccion = request.POST['direccion'], 
        telefono = request.POST['telefono'],  
        correo_electronico = request.POST['correo_electronico']
    )
    cliente.save()
    return redirect('/clientes-list')

def eliminarCliente(_request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete();
    return redirect('/clientes-list')