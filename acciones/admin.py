from django.contrib import admin
from .models import Accion,CompraAccion,ResultadoEconomico,CEOEmpresa

# Register your models here.
admin.site.register(Accion)
admin.site.register(CompraAccion)
admin.site.register(ResultadoEconomico)
admin.site.register(CEOEmpresa)