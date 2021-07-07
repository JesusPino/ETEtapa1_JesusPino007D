from django.shortcuts import render,redirect
from .models import Colaborador
from .forms import ColaboradorForm
# Create your views here.

def ventanaprincipal(request):
    return render(request, 'ventanaprincipal.html')

def anadir(request):
    return render(request, 'caosnews/anadir.html')    

def mostrar(request):
    colaboradores = Colaborador.objects.all()
    return render(request,'caosnews/mostrar.html',context={'colaboradores':colaboradores})

def anadir(request):
    if request.method =='POST':
        colaborador_form=ColaboradorForm(request.POST, request.FILES)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('mostrar')
    else:
        colaborador_form=ColaboradorForm()
    return render(request,'caosnews/anadir.html', {'colaborador_form':ColaboradorForm})

def modificar(request,id):
    colaborador = Colaborador.objects.get(rutt=id)
    datos={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method == 'POST':
        formulario = ColaboradorForm(data=request.POST, instance = colaborador)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar')
    return render(request, 'caosnews/modificar.html', datos)

def eliminar(request,id):
    colaborador = Colaborador.objects.get(rutt=id)
    colaborador.delete()
    return redirect('mostrar')
