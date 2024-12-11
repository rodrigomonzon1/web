from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    direccion = models.TextField(verbose_name="Dirección", blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")

    def __str__(self):
        return f"{self.nombre}, {self.apellido} - {self.email}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-fecha_registro"]
