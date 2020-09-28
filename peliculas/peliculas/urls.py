"""peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from appmovies.views import InicioView, PeliculaView, CrearPeliculaView, EditarPeliculaView, EliminarPeliculaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('pelicula/', PeliculaView.as_view(), name='pelicula'),
    
    path('crear_pelicula/', CrearPeliculaView.as_view(), name='crear_pelicula'),
    path('editar_pelicula/<int:pk>/',
         EditarPeliculaView.as_view(), name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>/',
         EliminarPeliculaView.as_view(), name='eliminar_pelicula'),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
