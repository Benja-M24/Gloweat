from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductForm

def list_prod(request):
    productos = Producto.objects.all()
    return render(request,'products.html',{'productos':productos})

def crear_prod(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_url')
    return render(request,'productos_form.html',{'form':form})

def editar_prod(request,id):
    productos = Producto.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=productos)

    if form.is_valid():
        form.save()
        return redirect('list_prod')

    return render(request, 'productos_form.html', {form:form, 'productos': productos})

def borrar_prod(request,id):
    productos = Producto.objects.get(id=id)

    if request.method == 'POST':
        productos.delete()
        return redirect('list_prod')

    return render(request, 'prod-delete-confirm.html', {'productos':productos})