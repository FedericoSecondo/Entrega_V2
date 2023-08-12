from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Accion, CompraAccion, ResultadoEconomico, CEOEmpresa,ETF,bkn
from .forms import AgregarAccionForm
from .forms import CEOEmpresaForm
from .forms import ResultadoEconomicoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import ETFForm
from .forms import BKNForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuariosForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    return render(request,"acciones/base.html")

""" def lista_acciones(request):
   acciones = Accion.objects.all()
   return render(request, 'acciones/lista_acciones.html', {'acciones': acciones}) """
@login_required
def lista_compras(request):
    compras = CompraAccion.objects.all()
    return render(request, 'acciones/lista_compras.html', {'compras': compras})
@login_required
def lista_resultados_economicos(request):
    resultados = ResultadoEconomico.objects.all()
    return render(request, 'acciones/lista_resultados_economicos.html', {'resultados': resultados})
@login_required
def lista_ceos(request):
    ceos = CEOEmpresa.objects.all()
    return render(request, 'acciones/lista_ceos.html', {'ceos': ceos})
@login_required
def lista_etf(request):
    ctx={"etf":ETF.objects.all()}
    return render(request,"acciones/lista_etf.html",ctx)
@login_required
def lista_bkn(request):
    bkn_objects = bkn.objects.all()
    return render(request, 'acciones/lista_bkn.html', {'bkn_objects': bkn_objects})


#-----------------------------------------------------------------------------------------------
#FORMULARIOS:
#-----------------------------------------------------------------------------------------------

#Esta seccion Contiene los Funciones para Crear


# Con esta Funcion Puedo Crear una nueva accion a monitorear
@login_required
def agregar_accion(request):
    if request.method == 'POST':
        form = AgregarAccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_acciones')  
    else:
        form = AgregarAccionForm()

    return render(request, 'acciones/agregar_accion.html', {'form': form})


# Con esta Funcion Puedo Crear una nueva informacion financiera de las empresas
@login_required
def agregar_ceo(request):
    if request.method == 'POST':
        form = CEOEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ceos')  
    else:
        form = CEOEmpresaForm()
    return render(request, 'acciones/agregar_ceo.html', {'form': form})

# Con esta Funcion Puedo Crear una nueva informacion sobre resultados economicos
@login_required
def agregar_resultado(request):
    if request.method == 'POST':
        form = ResultadoEconomicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_resultados')
    else:
        form = ResultadoEconomicoForm()
    
    return render(request, 'acciones/agregar_resultado.html', {'form': form})

# Con esta Funcion Puedo Crear nuevos ETFs a monitoreas
@login_required
def agregar_etf(request):
    if request.method == 'POST':
        form = ETFForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etfs')
    else:
        form = ETFForm()

    return render(request, 'acciones/agregar_etf.html', {'form': form})

# Con esta funcion puedo crear nuevas Nreaking News
@login_required
def agregar_bkn(request):
    if request.method == 'POST':
        form = BKNForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_bkn')
    else:
        form = BKNForm()
    
    ctx = {'form': form}
    return render(request, 'acciones/agregar_bkn.html', ctx)

#Falta una funcion para crear nuevas acciones compradas (Hay algun tema con el usuario, y eso me esta dificultando la creacion, revisar)

#------------------------------------------------------------------------------
#CRUDS (Update y Delete)
#------------------------------------------------------------------------------


#Con esta Funcion puedo realizar Updates (Editar) las acciones a monitorear
@login_required
def lista_acciones(request):
    ctx={"acciones":Accion.objects.all()}
    return render(request,"acciones/lista_acciones.html",ctx)

@login_required
def updateAccion(request, id_accion):
    accion = Accion.objects.get(id=id_accion)

    if request.method == "POST":
        miForm = AgregarAccionForm(request.POST, instance=accion)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy("lista_acciones"))
    else:
        miForm = AgregarAccionForm(instance=accion)

    return render(request, "acciones/agregar_accion.html", {"form": miForm})

#Con esta Funcion puedo realizar Delete (Borrar) las acciones a monitorear
@login_required
def deleteAccion(request, id_accion):
    accion = get_object_or_404(Accion, id=id_accion)
    
    if request.method == "POST":
        accion.delete()
        return redirect(reverse_lazy("lista_acciones"))
    
    return render(request, "acciones/delete_accion.html", {"accion": accion})

#Con esta Funcion puedo realizar Updates (Editar) la informacion financiera de empresas
@login_required
def editar_ceo(request, ceo_id):
    try:
        ceo = CEOEmpresa.objects.get(id=ceo_id)
    except CEOEmpresa.DoesNotExist:
        return redirect('lista_ceos')

    if request.method == 'POST':
        form = CEOEmpresaForm(request.POST, instance=ceo)
        if form.is_valid():
            form.save()
            return redirect('lista_ceos')
    else:
        form = CEOEmpresaForm(instance=ceo)

    return render(request, 'acciones/agregar_ceo.html', {'form': form})


#Con esta Funcion puedo realizar Deletes (Borrar) la informacion financiera de empresas
@login_required
def eliminar_ceo(request, id_ceo):
    ceo = CEOEmpresa.objects.get(pk=id_ceo)
    
    if request.method == 'POST':
        ceo.delete()
        return redirect('lista_ceos')
    
    return render(request, 'acciones/eliminar_ceo.html', {'ceo': ceo})


#Con esta funcion puedo editar ETFs

@login_required
def editar_etf(request, etf_id):
    try:
        etf = ETF.objects.get(id=etf_id)
    except ETF.DoesNotExist:
        etf = None

    if etf is None:
        return redirect('lista_etfs')

    if request.method == 'POST':
        form = ETFForm(request.POST, instance=etf)
        if form.is_valid():
            form.save()
            return redirect('lista_etfs')
    else:
        form = ETFForm(instance=etf)

    return render(request, 'acciones/editar_etf.html', {'form': form, 'etf': etf})

# Con esta funcion puedo eliminar ETFs
@login_required
def eliminar_etf(request, etf_id):
    try:
        etf = ETF.objects.get(id=etf_id)
    except ETF.DoesNotExist:
        etf = None

    if etf is not None and request.method == 'POST':
        etf.delete()
        return redirect('lista_etfs')

    return render(request, 'acciones/eliminar_etf.html', {'etf': etf})


# Con esta funcion puedo editar Breaking News
@login_required
def editar_bkn(request, bkn_id):
    template_name = 'acciones/editar_bkn.html'
    bkn_obj = bkn.objects.get(pk=bkn_id)
    
    if request.method == 'POST':
        form = BKNForm(request.POST, instance=bkn_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_bkn')
    else:
        form = BKNForm(instance=bkn_obj)
    
    return render(request, template_name, {'form': form})

# Con esta funcion puedo borrar Breaking News
@login_required
def borrar_bkn(request, bkn_id):
    template_name = 'acciones/borrar_bkn.html'
    bkn_obj = bkn.objects.get(pk=bkn_id)
    
    if request.method == 'POST':
        bkn_obj.delete()
        return redirect('lista_bkn')
    
    return render(request, template_name, {'bkn_obj': bkn_obj})

#---------------------------------------------------------------------------------------------------------
# A traves de esta vista genero un espacio para hablar sobre mi, tal como solicita la pauta de evaluacion
#---------------------------------------------------------------------------------------------------------

def federico_secondo(request):
    return render(request, 'acciones/federico_secondo.html')

#---------------------------------------
#Class Base View

#Cuando vi esto en la clase ya habia avanzado en el proyecto :) :)

#----------------------------------------------------------------

#Log in, Log out y Registracion

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "acciones/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "acciones/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "acciones/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "acciones/login.html", {"form":miForm})  

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "acciones/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "acciones/registro.html", {"form": form}) 


