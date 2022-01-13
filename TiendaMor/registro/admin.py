from django.contrib import admin
from .models import Datos

# Register your models here.
class DatosAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Datos,DatosAdmin)