from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import noticia

from account.decorators import mechanic_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator([login_required, mechanic_required], name='dispatch')
class IndexListView(ListView):
    model = noticia
    template_name='notices/index.html'
    context_object_name = 'noticias'
    paginate_by=6
@method_decorator([login_required, mechanic_required], name='dispatch')
class verDetailView(DetailView):
    model = noticia
    template_name = "notices/detail.html"
    success_url = reverse_lazy('notices:listanoticias')
@method_decorator([login_required, mechanic_required], name='dispatch')
class noticiaUpdateView(UpdateView):
    model = noticia
    template_name = "notices/edit.html"
    fields=['Titulo', 'Texto', 'Foto']
    success_url = reverse_lazy('notices:listanoticias')
@method_decorator([login_required, mechanic_required], name='dispatch')
class nuevaCreateView(CreateView):
    model = noticia
    template_name = "notices/create.html"
    fields=['Titulo', 'Texto', 'Foto']
    success_url = reverse_lazy('notices:listanoticias')
    def form_valid(self, form):
        form.instance.Autor = self.request.user
        return super(nuevaCreateView, self).form_valid(form)
@method_decorator([login_required, mechanic_required], name='dispatch')
class borrarDeleteView(DeleteView):
    model = noticia
    template_name = "notices/delete.html"
    success_url = reverse_lazy('notices:listanoticias')