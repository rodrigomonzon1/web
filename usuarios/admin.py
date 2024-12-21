from django.contrib import admin
from .models import Usuario, InfoUsuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'edad', 'fecha_creacion')
    search_fields = ('nombre', 'email')
    list_filter = ('edad',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(InfoUsuario)