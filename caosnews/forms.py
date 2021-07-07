from django import forms
from django.forms import ModelForm,widgets
from .models import Colaborador




class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields =['rutt','nombree','fotoo','emaill','telefonoo','diree','paiss','contraa']
        labels={
            'rutt': 'rut: ',
            'nombree': 'nombre: ',
            'fotoo': 'foto',
            'emaill': 'email: ',
            'telefonoo': 'telefono: ',
            'diree': 'direcion: ',
            'paiss': 'pais: ',
            'contraa': 'contraseña: ',
        }
        widgets={
            'rutt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rutt',
                    'placeholder': 'su rut'
                }
            ),
            'nombree': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombree',
                    'placeholder': 'su nombre'
                }
            ),
            'fotoo': forms.FileInput(
                
            ),
            'emaill': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'emaill',
                    'placeholder': 'su email'
                }
            ),
            'telefonoo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefonoo',
                    'placeholder': 'su telefono'
                }
            ),
            'diree': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'diree',
                    'placeholder': 'su direccion'
                }
            ),
            'paiss': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'paiss',
                    'placeholder': 'su pais'
                }
            ),
            'contraa': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contraa',
                    'placeholder': 'su contraseña'
                }
            )

        }
