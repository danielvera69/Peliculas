from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'tipoPelicula', 'poster', 'sipnosis', 'duracion',
                  'clasificacion', 'trailer', 'estado')
        label = {
            'titulo': 'Titulo',
            'tipoPelicula': 'Tipo de Pelicula',
            'poster': 'Poster',
            'sipnosis': 'Sipnosis',
            'duracion': 'Duracion',
            'clasificacion': 'Clasificacion',
            'trailer': 'Trailer',
            'estado': 'Estado'
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipoPelicula': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'poster': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sipnosis': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'clasificacion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
