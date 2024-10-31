from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
from django.core.mail import EmailMessage
from django.conf import settings

def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'app_comentarios/lista_comentarios.html', {'comentarios': comentarios})

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            #enviar notificacion al correo
            email = EmailMessage(
                'Nuevo Comentario',
                f'Se ha ingresado un nuevo comentario:\n\nNombre: {comentario.nombre}\nCorreo: {comentario.email}\nComentario: {comentario.comentario}',
                comentario.email,
                ['proyectoamadgti.eq2@gmail.com'],
                reply_to=[comentario.email]
            )
            email.send(fail_silently=False)
            return redirect('lista_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'app_comentarios/agregar_comentario.html', {'form': form})
