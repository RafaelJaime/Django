from django.urls import include, path
from . import views
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
app_name='notices'

urlpatterns = [
    path("", views.IndexListView.as_view(), name="listanoticias"),
    path("editar/<int:pk>", views.noticiaUpdateView.as_view(), name="editarnoticia"),
    path('<int:pk>', views.verDetailView.as_view(), name="vernoticia"),
    path('nueva', views.nuevaCreateView.as_view(), name="nuevanoticia"),
    path("borrar/<pk>", views.borrarDeleteView.as_view(), name="borrarnoticia")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
