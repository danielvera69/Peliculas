from .models import Pelicula
from .forms import PeliculaForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


class InicioView(TemplateView):
    template_name = "index.html"

# vistas de Peliculas


class PeliculaView(ListView):
    model = Pelicula
    template_name = "peliculas/pelicula.html"
    context_object_name = "peliculas"
    #queryset = Pelicula.objects.filter(titulo="avenger")


class CrearPeliculaView(CreateView):
    model = Pelicula
    template_name = "peliculas/registrar_pelicula.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula')


class EditarPeliculaView(UpdateView):
    model = Pelicula
    template_name = "peliculas/registrar_pelicula.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula')


class EliminarPeliculaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        pelicula = Pelicula.objects.get(id=pk)
        pelicula.delete()
        # object.estado = False
        # object.save()
        return redirect('pelicula')
# vistas de Historial
