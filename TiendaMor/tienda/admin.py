from django.contrib import admin
from .models import Producto, CategoriaProducto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Producto,ProductoAdmin)
admin.site.register(CategoriaProducto,CategoriaProductoAdmin)