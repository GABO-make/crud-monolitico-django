from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock']
    list_filter = ['precio', 'stock']
    search_fields = ['nombre', 'descripcion']
