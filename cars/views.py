from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import coche
import datetime

from account.decorators import client_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator([login_required, client_required], name='dispatch')
class IndexListView(ListView):
    model = coche
    template_name='cars/index.html'
    context_object_name = 'coches'
    paginate_by=8
    def get_queryset(self, *args, **kwargs):
        return coche.objects.filter(Dueno=self.request.user.id)
@method_decorator([login_required, client_required], name='dispatch')
class cocheCreateView(CreateView):
    model = coche
    template_name = "cars/create.html"
    fields=['Matricula', 'Marca', 'Modelo', 'Color', 'FechaMatriculacion','Imagen']
    success_url = reverse_lazy('cars:listacoches')
    anos = []
    for i in range(30):
        anos.append(datetime.date.today().year - i)
    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        form = super(CreateView, self).get_form()
        form.fields['FechaMatriculacion'].widget = SelectDateWidget(years=self.anos)
        return form
    def form_valid(self, form):
        form.instance.Dueno = self.request.user
        return super(cocheCreateView, self).form_valid(form)
@method_decorator([login_required, client_required], name='dispatch')
class verDetailView(DetailView):
    model = coche
    template_name="cars/detail.html"
    success_url = reverse_lazy('cars:listacoches')
@method_decorator([login_required, client_required], name='dispatch')
class editarUpdateView(UpdateView):
    anos = []
    for i in range(30):
        anos.append(datetime.date.today().year - i)
    model = coche
    template_name = "cars/edit.html"
    fields=['Matricula', 'Marca', 'Modelo', 'Color', 'FechaMatriculacion','Imagen']
    success_url = reverse_lazy('cars:listacoches')
    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        form = super(UpdateView, self).get_form()
        form.fields['FechaMatriculacion'].widget = SelectDateWidget(years=self.anos)
        return form
    def form_valid(self, form):
        form.instance.Dueno = self.request.user
        return super(editarUpdateView, self).form_valid(form)
@method_decorator([login_required, client_required], name='dispatch')
class borrarDeleteView(DeleteView):
    model = coche
    template_name = "cars/delete.html"
    success_url = reverse_lazy('cars:listacoches')