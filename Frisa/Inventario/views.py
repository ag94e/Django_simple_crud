from django.shortcuts import render, redirect
from .models import ModeloInventario
from .forms import FormularioInventario


def inicio(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        cod = request.POST['codigo']
        modelo = ModeloInventario.objects.filter(codigo=cod)
        if modelo.exists():
            return render(request, 'index.html', {'modelo': modelo})
        else:
            contexto = {
                'no_existe': f'El código {cod} no existe',
            }
            return render(request, 'index.html', contexto)

    return render(request, 'index.html', {'modelo': modelo})
        


def agregar(request):   
    form = FormularioInventario()

    if request.method == 'POST':
        form = FormularioInventario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventarios:inicio')
    else:
        form = FormularioInventario()
    
    return render(request, 'agregar.html', {'form': form})


def modificar(request, pk):
    cod = ModeloInventario.objects.get(pk=pk)
    form = FormularioInventario(instance=cod)

    if request.method == 'POST':
        form = FormularioInventario(request.POST, instance=cod)
        if form.is_valid():
            cod = form.save(commit=False)
            cod.save()
            return redirect('inventarios:inicio')

    elif request.method == 'GET':
        if form.is_valid():
            return render(request, 'modificar.html', {'form': form})
    else:
        form = FormularioInventario()

    return render(request, 'modificar.html', {'form': form})


def eliminar(request, pk):
    cod = ModeloInventario.objects.get(pk=pk)
    cod.delete()
    return redirect('inventarios:inicio')
