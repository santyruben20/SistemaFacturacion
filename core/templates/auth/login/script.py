from django.shortcuts import redirect

def validarLogin(request):
    if validarCajero(request):
        return redirect('/cajeros-form/')

    if validarUsuario(request):
        return redirect('')

    if validarBodeguero(request):
        return redirect('/bodegueros-form/')
    return redirect('/login/')

def validarUsuario(request):
    email_usuario=request.POST['email_l']
    clave_usuario=request.POST['clave_l']

    try: 
        usuario_administrador.objects.get(email_usuario=email_usuario, clave_usuario=clave_usuario)
        return True
    except:
        return False 

def validarCajero(request):
    email_cajero=request.POST['email_l']
    clave_cajero=request.POST['clave_l']

    try: 
        cajero.objects.get(email_cajero=email_cajero, clave_cajero=clave_cajero)
        return True
    except:
        return False

def validarBodeguero(request):
    email_bodeguero=request.POST['email_l']
    clave_bodeguero=request.POST['clave_l']

    try: 
        bodeguero.objects.get(email_bodeguero=email_bodeguero, clave_bodeguero=clave_bodeguero)
        return True
    except:
        return False
