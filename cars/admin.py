from django.contrib import admin
from .models import coche
# Register your models here.
class CocheAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion basica',{'fields': ['Matricula', 'FechaMatriculacion', 'Dueno']}),
        ('Informacion extra', {'fields': ['Marca', 'Modelo', 'Color', 'Imagen'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'Matricula', 'FechaMatriculacion', 'Marca', 'Modelo', 'Dueno')
    search_fields = ['Matricula']
    list_filter = ['FechaMatriculacion', 'Marca']
admin.site.register(coche, CocheAdmin)