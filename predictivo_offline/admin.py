from django.contrib import admin

# Register your models here.

from .models import Medicion, Equipo, Sector, MiniPlanta

admin.site.register(Medicion)
admin.site.register(Equipo)
admin.site.register(Sector)
admin.site.register(MiniPlanta)
