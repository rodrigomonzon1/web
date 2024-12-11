from django.contrib import admin

# Register your models here.

from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_registro", "activo")
    search_fields = ("nombre", "apellido", "email")
    list_filter = ("activo", "fecha_registro")