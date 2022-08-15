from django.shortcuts import render

def print_from_button(request):
    if(request.GET.get('print_btn')):
        print('Button clicked')
    return render(request, 'new/click.html',{'value':'Button clicked'})

def agregarProducto():
    pritn('')