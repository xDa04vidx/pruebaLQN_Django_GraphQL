from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Director)
admin.site.register(Planeta)
admin.site.register(Pelicula)
admin.site.register(Productor)
admin.site.register(PeliculaPlaneta)
admin.site.register(PeliculaDirector)
admin.site.register(PeliculaPersonaje)
admin.site.register(PeliculaProductor)