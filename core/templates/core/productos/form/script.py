from django.shortcuts import redirect
from .....models import Producto

#registro de productos
def registroProducto(request):
    producto = Producto(
        nombre = request.POST['nombre'], 
        precio_actual = request.POST['precio_actual'], 
        marca = request.POST['marca'], 
        descuento = request.POST['descuento'],
        stock = request.POST['stock']
    )
    producto.save()
    return redirect('/productos-list/')