from django.contrib import admin
from .models import TipoPelicula, Pelicula
# Register your models here.


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipoPelicula', 'poster', 'sipnosis', 'duracion',
                    'clasificacion', 'estado')

    ordering = ('tipoPelicula',)
    search_fields = ('tipoPelicula', 'clasificacion', 'titulo')
    list_filter = (
        'tipoPelicula__descripcion',
        'estado',
    )


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(TipoPelicula)
