from django.contrib import admin

# Register your models here.
from apps.asientos_contables.models import *

admin.site.register(asientoContable)
admin.site.register(libroMayor)
#admin.site.register(libroDiario)
admin.site.register(cuenta)

