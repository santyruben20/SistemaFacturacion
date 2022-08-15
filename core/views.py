from django.shortcuts import render

from .models import Bodeguero, Cajero, Categoria, Cliente, Factura, Producto, UsuarioAdministrador

# Create your views here.

def admin(request):
    return render(request,'admin/admin.html', {})

# authentication
def login(request):
    return render(request,'auth/login/login.html')

def registro(request):
    return render(request,'auth/registro/registro.html')

# usuarios
def usuariosForm(request):
    return render(request,'admin/usuarios/form/usuarios-form.html')

def usuariosList(request):
    usuarios = UsuarioAdministrador.objects.all()
    context = {"usuarios": usuarios}
    return render(request,'admin/usuarios/list/usuarios-list.html', context)

# bodeguero
def bodegueroForm(request):
    return render(request,'core/bodeguero/form/bodeguero-form.html')

def bodegueroList(request):
    bodegueros = Bodeguero.objects.all()
    context = {"bodegueros": bodegueros}
    return render(request,'core/bodeguero/list/bodeguero-list.html', context)

# cajero
def cajeroForm(request):
    return render(request,'core/cajero/form/cajero-form.html')

def cajeroList(request):
    cajeros = Cajero.objects.all()
    context = {"cajeros": cajeros}
    return render(request,'core/cajero/list/cajero-list.html', context)

# clientes
def clientesForm(request):
    return render(request,'core/clientes/form/clientes-form.html')

def clientesList(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request,'core/clientes/list/clientes-list.html', context)

# categorias
def categoriasForm(request):
    return render(request,'core/categorias/form/categorias-form.html')

def categoriasList(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'core/categorias/list/categorias-list.html', context)

# productos
def productosForm(request):
    return render(request,'core/productos/form/productos-form.html')

def productosList(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request,'core/productos/list/productos-list.html', context)

# productos
def facturasForm(request):
    return render(request,'core/facturas/form/facturas-form.html')

def facturasList(request):
    facturas = Factura.objects.all()
    context = {"facturas": facturas}
    return render(request,'core/facturas/list/facturas-list.html', context)

# productos
def preformasForm(request):
    return render(request,'core/preformas/form/preformas-form.html')
