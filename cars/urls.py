from django.urls import include, path
from . import views
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
app_name='cars'

urlpatterns = [
    path("", views.IndexListView.as_view(), name="listacoches"),
    path("nuevo", views.cocheCreateView.as_view(), name="nuevocoche"),
    path('<int:pk>', views.verDetailView.as_view(), name="vercoche"),
    path('editar/<int:pk>', views.editarUpdateView.as_view(), name="editarcoche"),
    path("borrar/<pk>", views.borrarDeleteView.as_view(), name="borrarcoche")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
