from django.shortcuts import render, redirect
from .form import Usuarioform
from .models import Usuario

def Home(request):
    return render(request, 'login.html')
 
def CrearUsuario(request):
    if request.method== 'POST':
        Usuario_Form = Usuarioform(request.POST)
        if Usuario_Form.is_valid():
            Usuario_Form.save()
            return redirect('crear_usuario') 
    else:
        Usuario_Form = Usuarioform()
    return render(request, 'login/login.html',{'Usuario_Form':Usuario_Form})

def ListarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista/lista.html', {'usuarios':usuarios} )