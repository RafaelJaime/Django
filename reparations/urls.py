from django.urls import include, path
from . import views

app_name='reparations'

urlpatterns = [
    path("reparate/<int:pk>", views.reparateView, name="reparate"),
    path("reparations", views.reparationView.as_view(), name="reparations"),
    path("mechanic_reparations", views.reparationMechanicView.as_view(), name="Mreparations"),
    path("mechanic_reparate", views.reparateMechanicView.as_view(), name="Mreparate"),
    path("mechanic_reparate/<int:pk>", views.reparMechanicView, name="Mrepar"),
    path("report/<int:pk>", views.informeView.as_view(), name="report"),
]