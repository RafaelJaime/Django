from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib import messages

from django.conf import settings
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from datetime import date

from cars.models import coche
from account.models import User

from .models import reparation
from .forms import ReparateForm

from account.decorators import client_required, mechanic_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@client_required
def reparateView(request, pk):
    form = ReparateForm(request.POST or None)
    coche1 = coche.objects.get(pk=pk)

    if request.method == 'GET':
        return render(request, 'reparations/reparate.html', {
            'coche': coche1,
            'usuario': request.user,
            'form': form,
        }, )

    if request.method == 'POST':
        reparacion = reparation
        if form.is_valid():
            try:
                reparacion = reparation.objects.get(Coche=coche1, Arreglado=False)
                reparation.objects.filter(Coche=coche1).update(Motivo=request.POST.get('Motivo'))
                reparation.refresh_from_db()
                messages.error(request, 'Ya existe la petición de reparación, se actualizará el motivo.')
            except reparacion.DoesNotExist:
                reparacion = reparation(Motivo=request.POST.get('Motivo'),Coche=coche1, Dueno = request.user)
                messages.success(request, 'Petición para reparación realizada correctamente.')
            reparacion.save()
            return redirect('index')

@method_decorator([login_required, client_required], name='dispatch')
class reparationView(ListView):
    model = reparation
    template_name = 'reparations/index.html'
    context_object_name = "reparaciones"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return reparation.objects.filter(Dueno=self.request.user.id).order_by('-FechaArreglo')


@method_decorator([login_required, mechanic_required], name='dispatch')
class reparationMechanicView(ListView):
    model = reparation
    template_name = 'reparations/index.html'
    context_object_name = "reparaciones"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return reparation.objects.filter(Mecanico=self.request.user.id, Arreglado=True)


@method_decorator([login_required, mechanic_required], name='dispatch')
class reparateMechanicView(ListView):
    model = reparation
    template_name = 'reparations/reparateIndex.html'
    context_object_name = "reparaciones"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return reparation.objects.filter(Arreglado=False).order_by('FechaSolicitud')
@method_decorator([login_required, mechanic_required], name='dispatch')
class informeView(View):
    def cabecera(self, pdf):
        img = settings.BASE_DIR + '/static/logo.jpg'
        pdf.drawImage(img, 40, 700, 500, 120, preserveAspectRatio=True)
        for i in range(490):
            pdf.drawString(50+i, 690, u"-")
        pdf.drawString(
            50, 670, u"Fecha: " +
            str(date.today())
        )

    def cuerpo(self, pdf, reparation):
        s = 500
        pdf.setFont("Helvetica", 16)
        pdf.drawString(50, s, u"Reporte de la reparación: ")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(
            50, s-30, u"Fecha de solicitud: " +
            str(reparation.FechaSolicitud.date())
        )
        pdf.drawString(
            50, s-50,u"Dueño: " + reparation.Dueno.get_full_name() + "  Coche: " + reparation.Coche.Matricula
        )
        pdf.drawString(
            50, s-70, u"Motivo: " + reparation.Motivo 
        )
        pdf.drawString(
            50, s-120, u"Fecha de reparación: " + str(reparation.FechaArreglo.date())
        )
        pdf.drawString(
            50, s-140, u"Mecánico: " + reparation.Mecanico.get_full_name()
        )
        pdf.drawString(
            50, s-160, u"Observaciones: " + str(reparation.Observaciones)
        )
            

    def pie(self, pdf):
        pdf.drawString(50, 45, u"Teloreparo©")
        for i in range(490):
            pdf.drawString(50+i, 55, u"-")

    def get(self, request, pk, *args, **kwargs):
        response = HttpResponse(content_type="application/pdf")
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("report" + str(pk) + ".pdf")
        self.cabecera(pdf)
        rp = reparation.objects.get(id=pk)
        self.cuerpo(pdf, rp)
        self.pie(pdf)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
