from django.db import models
from django.conf import settings

#------------------------------------
# MIS MODELOS
#------------------------------------
from django.db import models

class Accion(models.Model):
    simbolo = models.CharField(max_length=10)
    descripcion = models.TextField(default="Descripción", max_length=255)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.simbolo

class CompraAccion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    simbolo = models.CharField(max_length=10)
    cantidad = models.PositiveIntegerField()
    precio = models.PositiveIntegerField(default=1)
    fecha_compra = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.simbolo} ({self.cantidad} acciones)"
    
class ResultadoEconomico(models.Model):
    accion_comprada = models.OneToOneField(CompraAccion, on_delete=models.CASCADE)
    resultado_ultimo_anio = models.DecimalField(max_digits=10, decimal_places=2)
    proyeccion_proximo_anio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Resultado de {self.accion_comprada.simbolo}"

class CEOEmpresa(models.Model):
    accion = models.OneToOneField(Accion, on_delete=models.CASCADE)
    nombre_director = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    sitio_web = models.URLField()

    def __str__(self):
        return f"CEO de {self.accion.simbolo}: {self.nombre_director}"
    
#----------------------------------------------------------------
class ETF(models.Model):
    simbolo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=10)
    subyacente = models.CharField(max_length=10)
    precioTarget=models.PositiveIntegerField(default=1)

class bkn(models.Model):
    empresa = models.CharField(max_length=50)
    titular = models.CharField(max_length=50)

