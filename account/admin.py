from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from . import forms
# Register your models here.


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Specialities: ',
            {
                'fields': (
                    'dni',
                    'direction',
                    'telephone',
                    'bornDate',
                    'is_client',
                    'is_mechanic',
                ),
            },
        ),
    )
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_client', 'is_mechanic', 'is_active')
    list_filter = ['is_client', 'is_mechanic']
admin.site.register(User, UserAdmin)