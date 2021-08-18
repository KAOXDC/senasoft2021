from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate

''' Modulo Auto '''

def lista_autos (request):
    # consulta a la tabla Auto y retornamos una lista de autos
    lista = Auto.objects.filter()
    return render (request, 'autos/lista_autos.html', locals()) 

def agregar_auto (request):
    if request.method == 'POST':
        formulario = agregar_auto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('/autos/lista/')
    else: # es un methodo GET
        formulario = agregar_auto_form() # crear un formulario vacio del modelo Auto

    return render (request, 'autos/agregar_auto.html', locals()) 

def detalle_auto (request, id_auto):
    carro = Auto.objects.get(id = id_auto)
    # SELECT * FROM Auto WHERE (id == id_auto)
    return render (request, 'autos/detalle_auto.html', locals()) 

def editar_auto (request, id_auto):
    carro = Auto.objects.get(id = id_auto)
    if request.method == 'POST':
        formulario = agregar_auto_form(request.POST, request.FILES, instance= carro)
        if formulario.is_valid():
            formulario.save()
            return redirect('/autos/lista/')
    else:
        formulario = agregar_auto_form(instance = carro)
    return render (request, 'autos/editar_auto.html', locals()) 

def eliminar_auto (request, id_auto):
    carro = Auto.objects.get(id = id_auto)
    carro.delete()
    return redirect('/autos/lista/')

''' Modulo Marca '''

def lista_marcas (request):
    # consulta a la tabla marca y retornamos una lista de marcas
    lista = Marca.objects.filter()
    vista = 'Marca'
    return render (request, 'autos/lista_marcas.html', locals()) 

def agregar_marca (request):
    if request.method == 'POST':
        formulario = agregar_marca_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('/lista_marca/')
    else: # es un methodo GET
        formulario = agregar_marca_form() # crear un formulario vacio del modelo marca

    return render (request, 'autos/agregar_marca.html', locals()) 

def detalle_marca (request, id_marca):
    carro = Marca.objects.get(id = id_marca)
    # SELECT * FROM marca WHERE (id == id_marca)
    return render (request, 'autos/detalle_marca.html', locals()) 

def editar_marca (request, id_marca):
    carro = Marca.objects.get(id = id_marca)
    if request.method == 'POST':
        formulario = agregar_marca_form(request.POST, request.FILES, instance= carro)
        if formulario.is_valid():
            formulario.save()
            return redirect('/autos/lista_marca/')
    else:
        formulario = agregar_marca_form(instance = carro)
    return render (request, 'autos/editar_marca.html', locals()) 

def eliminar_marca (request, id_marca):
    carro = Marca.objects.get(id = id_marca)
    carro.delete()
    return redirect('/autos/lista_marca/')

'''
Autenticación
'''

def vista_login (request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/autos/lista/')
            else: 
                msj = 'usuario o clave incorrectos'
    
    formulario = login_form()
    return render(request, 'autos/login.html', locals())

def vista_logout (request):
    logout(request)
    return redirect('/autos/login/')
