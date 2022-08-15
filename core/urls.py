from django.urls import path

from .templates.core.clientes.form.script import registroCliente

from .templates.core.productos.form.script import registroProducto

from .templates.core.categorias.form.script import registroCategoria

from .templates.core.cajero.form.script import registroCajero

from .templates.core.facturas.list.script import eliminarFactura

from .templates.core.productos.list.script import eliminarProducto

from .templates.core.clientes.list.script import eliminarCliente

from .templates.core.categorias.list.script import eliminarCategoria

from .templates.core.cajero.list.script import eliminarCajero

from .templates.core.bodeguero.form.script import eliminarBodeguero, registroBodeguero

from .templates.admin.usuarios.list.script import eliminarUsuario
from .views import admin, login, registro, usuariosForm, usuariosList, bodegueroForm, bodegueroList, cajeroForm, cajeroList, clientesForm, clientesList, categoriasForm, categoriasList, productosForm, productosList, preformasForm, facturasForm, facturasList

from .templates.auth.login.script import validarLogin
from .templates.admin.usuarios.form.script import registroUsuario

urlpatterns = [
    path('', admin),
    path('login/', login),
    path('registro/', registro),
    
    path('usuarios-form/', usuariosForm),
    path('usuarios-list/', usuariosList),
    path('validar-registro-usuarios/', registroUsuario, name = "validar-registro-usuarios"),
    path('eliminar_usuario/<int:id>/',eliminarUsuario,name = 'eliminar_usuario'),

    path('bodegueros-form/', bodegueroForm),
    path('bodegueros-list/', bodegueroList),
    path('registro_bodeguero/', registroBodeguero, name = "registro_bodeguero"),
    path('eliminar_bodeguero/<int:id>/', eliminarBodeguero, name = "eliminar_bodeguero"),

    path('cajeros-form/', cajeroForm),
    path('cajeros-list/', cajeroList),
    path('registro_cajero/', registroCajero, name = "registro_cajero"),
    path('eliminar_cajero/<int:id>/', eliminarCajero, name = "eliminar_cajero"),

    path('clientes-form/', clientesForm),
    path('clientes-list/', clientesList),
    path('registro_cliente/', registroCliente, name = "registro_cliente"),
    path('eliminar_cliente/<int:id>/', eliminarCliente, name = "eliminar_cliente"),

    path('categorias-form/', categoriasForm),
    path('categorias-list/', categoriasList),
    path('registro_categoria/', registroCategoria, name = "registro_categoria"),
    path('eliminar_categoria/<int:id>/', eliminarCategoria, name = "eliminar_categoria"),

    path('productos-form/', productosForm),
    path('productos-list/', productosList),
    path('registro_producto/', registroProducto, name = "registro_producto"),
    path('eliminar_producto/<int:id>/', eliminarProducto, name = "eliminar_producto"),

    path('preformas-form/', preformasForm),

    path('facturas-form/', facturasForm),
    path('facturas-list/', facturasList),
    path('eliminar_factura/<int:id>/', eliminarFactura, name = "eliminar_factura"),






    path('validar-login/', validarLogin, name = "validar-login"),
]
