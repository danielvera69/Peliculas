# Generated by Django 3.0 on 2020-09-21 15:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo de Pelcula',
                'verbose_name_plural': 'Tipos de Pelculas',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('metodo_pago', models.CharField(choices=[('C', 'Contado'), ('T', 'Tarjeta')], default='C', max_length=1)),
                ('preferencias', models.TextField(verbose_name='Preferencias de Peliculas')),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo Pelicula')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='poster/', verbose_name='Poster Pelicula')),
                ('sipnosis', models.TextField(verbose_name='Sipnosis')),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Duracion pelicula')),
                ('clasificacion', models.CharField(choices=[('T', 'Todo Publico'), ('N', 'Niños menores de 12 años'), ('A', 'Mayores de 18 años')], default='T', max_length=1, verbose_name='Clasificacion Pelicula')),
                ('trailer', models.URLField(max_length=500, verbose_name='Trailer Pelicula')),
                ('estado', models.BooleanField(default=True)),
                ('tipoPelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appmovies.TipoPelicula')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pelcula',
                'verbose_name_plural': 'Pelculas',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.datetime(2020, 9, 21, 10, 8, 15, 629340), null=True)),
                ('estado', models.BooleanField(default=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appmovies.Pelicula')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historiales',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.date(2020, 9, 21), null=True)),
                ('estado', models.BooleanField(default=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appmovies.Pelicula')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
                'ordering': ['fecha'],
            },
        ),
    ]
