from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Servicio)
admin.site.register(Turista)
admin.site.register(Empresa)
admin.site.register(ServicioEmpresa)
admin.site.register(PagoEmpresa)
admin.site.register(Paquete)
admin.site.register(ReservaPago)