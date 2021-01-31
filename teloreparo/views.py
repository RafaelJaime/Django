from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from notices.models import noticia
def index_view(request):
    noticias = noticia.objects.order_by('-Fcreacion');
    return render(request, 'index.html', {
        'noticias': noticias,
    }, )