from django.contrib import admin
from .models import reparation
# Register your models here.
class ReparationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion basica',{'fields': ['Coche', 'Dueno', 'Motivo', 'Arreglado']}),
        ('Informacion extra', {'fields': [ 'Observaciones', 'Mecanico'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'Coche', 'Dueno', 'Arreglado')
    search_fields = ['Dueno', 'Coche']
    list_filter = ['Arreglado']
admin.site.register(reparation, ReparationAdmin)