from unicodedata import name
from django.conf import settings
from django.db import models
from django.utils import timezone

class Bodeguero(models.Model):
    nombres = models.CharField(max_length=100, name = "nombres", null = False)
    apellidos = models.CharField(max_length=100, name = "apellidos", null = False)
    direccion = models.CharField(max_length=100, name = "direccion", null = False)
    telefono = models.CharField(max_length=50, name = "telefono", null = False)
    tipo_de_licencia = models.CharField(max_length=50, name = "tipo_de_licencia", null = False)
    email = models.CharField(max_length=50, name = "email", null = False)
    clave = models.CharField(max_length=50, name = "clave", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)
    
    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class Cajero(models.Model):
    nombres = models.CharField(max_length=100, name = "nombres", null = False)
    apellidos = models.CharField(max_length=100, name = "apellidos", null = False)
    direccion = models.CharField(max_length=100, name = "direccion", null = False)
    telefono = models.CharField(max_length=50, name = "telefono", null = False)
    exp_laboral = models.CharField(max_length=50, name = "exp_laboral", null = False)
    idiomas = models.CharField(max_length=50, name = "idiomas", null = False)
    email = models.CharField(max_length=50, name = "email", null = False)
    clave = models.CharField(max_length=50, name = "clave", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100, name = "descripcion", null = False)
    bodeguero = models.CharField(max_length=100, name = "bodeguero", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class Cliente(models.Model):
    cedula = models.CharField(max_length=100, name = "cedula", null = False)
    nombres = models.CharField(max_length=100, name = "nombres", null = False)
    apellidos = models.CharField(max_length=100, name = "apellidos", null = False)
    direccion = models.CharField(max_length=100, name = "direccion", null = False)
    telefono = models.CharField(max_length=100, name = "telefono", null = False)
    correo_electronico = models.CharField(max_length=100, name = "correo_electronico", null = False)
    cajero = models.CharField(max_length=100, name = "cajero", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class UsuarioAdministrador(models.Model):
    nombres = models.CharField(max_length=100, name = "nombres", null = False)
    apellidos = models.CharField(max_length=100, name = "apellidos", null = False)
    direccion = models.CharField(max_length=100, name = "direccion", null = False)
    telefono = models.CharField(max_length=100, name = "telefono", null = False)
    email = models.CharField(max_length=100, name = "email", null = False)
    clave = models.CharField(max_length=100, name = "clave", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class Producto(models.Model):
    nombre = models.CharField(max_length=50, name = "nombre", null = False)
    precio_actual = models.CharField(max_length=50, name = "precio_actual", null = False)
    marca = models.CharField(max_length=50, name = "marca", null = False)
    descuento = models.CharField(max_length=50, name = "descuento", null = False)
    stock = models.CharField(max_length=50, name = "stock", null = False)
    categoria = models.CharField(max_length=50, name = "categoria", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class Factura(models.Model):
    fecha = models.CharField(max_length=100, name = "fecha", null = False)
    cajero = models.CharField(max_length=100, name = "cajero", null = False)
    cliente = models.CharField(max_length=100, name = "cliente", null = False)
    usuario = models.CharField(max_length=100, name = "usuario", null = False)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()

class DetalleFactura(models.Model):
    cantidad = models.FloatField(max_length = 200, name = "cantidad", null = True)
    precio_unitario = models.FloatField(max_length = 200, name = "precio_unitario", null = True)
    importe = models.FloatField(max_length = 200, name = "importe", null = True)
    subtotal = models.FloatField(max_length = 200, name = "subtotal", null = True)
    iva = models.FloatField(max_length = 200, name = "iva", null = True)
    total = models.FloatField(max_length = 200, name = "total", null = True)
    factura = models.FloatField(max_length = 200, name = "factura", null = True)
    producto = models.FloatField(max_length = 200, name = "producto", null = True)
    creatAt = models.DateTimeField(name = "creat_at", null = True, blank = True)

    def publish(self):
        self.creat_at = timezone.now()
        self.save()
