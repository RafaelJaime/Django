from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from notices.models import noticia
from django.core.paginator import Paginator
from django.contrib import messages

from datetime import datetime

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def index_view(request):
    noticias = noticia.objects.order_by('-Fcreacion')
    paginator = Paginator(noticias, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {
        'noticias': page_obj
    }, )


def contactView(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        ahora = datetime.now()
        ahora = ahora.strftime("%m/%d/%Y a las %H:%M:%S")
        mensaje = request.POST.get('message')
        print(len(mensaje))
        if mensaje and mail and len(mensaje)>= 10:
            send_email(mail, ahora, mensaje)
            messages.success(request, 'Correo enviado correctamente.')
        else:
            messages.error(request, 'Correo o mensaje no válido.')
        return redirect('index')
    else:
        return render(request, 'contact.html', {})


def send_email(email, tiempo, mensaje):
    context = {'mail': email, 'time': tiempo, 'message': mensaje}
    template=get_template("correo.html")
    content = template.render(context)
    
    correo = EmailMultiAlternatives(
        'Teloreparo',
        'Contacto con administrador',
        email,
        [settings.EMAIL_HOST_USER]
    )
    correo.attach_alternative(content, 'text/html')
    correo.send()

def error_404(request, exception):
        data = {}
        return render(request,'errors/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'errors/error_500.html', data)