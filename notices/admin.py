from django.contrib import admin
from .models import noticia
# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion basica',{'fields': ['Titulo', 'Texto', 'Foto', 'Autor']}),
    ]
    list_display = ('Titulo', 'Autor')
    search_fields = ['Titulo', 'Autor']
admin.site.register(noticia, NoticiaAdmin)