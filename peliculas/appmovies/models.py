from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class TipoPelicula(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)

    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["descripcion"]
        verbose_name = "Tipo de Pelcula"
        verbose_name_plural = "Tipos de Pelculas"

    def __str__(self):
        return "{}".format(self.descripcion)


class Pelicula(models.Model):
    clasificacion_pelicula = (
        ('T', 'Todo Publico'), ('N', 'Niños menores de 12 años'), ('A', 'Mayores de 18 años'))
    titulo = models.CharField('Titulo Pelicula', max_length=100)
    tipoPelicula = models.ForeignKey(TipoPelicula, on_delete=models.PROTECT)
    poster = models.ImageField('Poster Pelicula',
                               upload_to='poster/', blank=True, null=True)
    sipnosis = models.TextField('Sipnosis')
    duracion = models.DecimalField(
        'Duracion pelicula', decimal_places=2, max_digits=10)

    clasificacion = models.CharField(
        'Clasificacion Pelicula', choices=clasificacion_pelicula, max_length=1, default='T')
    trailer = models.URLField('Trailer Pelicula', max_length=500)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)

    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Pelcula"
        verbose_name_plural = "Pelculas"

    def __str__(self):
        return "{}".format(self.titulo)


class Favorito(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True, default=date.today())
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["fecha"]
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return "{}".format(self.pelicula.titulo)


class Historial(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True, default=date.today())
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["fecha"]
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return "{}".format(self.pelicula.titulo)


class PerfilUsuario(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    metodo_pago = models.CharField(
        choices=(('C', 'Contado'), ('T', 'Tarjeta')), default='C', max_length=1)
    preferencias = models.TextField('Preferencias de Peliculas')
    estado = models.BooleanField(default=True)
