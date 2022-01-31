from django import forms
from .models import organizaciones


class EditarOrganizacionForm(forms.ModelForm):
    class Meta:
        model = organizaciones
        fields = [
            'identificación',
            'nombre_organizacion',
            'descripcion',
            'fecha_creacion',
            'fecha_registro',
            'correo',
            'telefono',
            'direccion1',
            'logo',
        ]
        labels = {
            'identificación': 'Identificacion',
            'nombre_organizacion': 'Nombre Organizacion',
            'descripcion': 'A que se dedica?',
            'fecha_creacion': 'Fecha de Creacion',
            'fecha_registro': 'Fecha de Registro',
            'correo': 'Correo Electronico',
            'telefono': 'Telefono',
            'direccion1': 'Direccion',
            'logo': 'Logo Organizacion',
        }
        widgets = {
            'identificación': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nombre_organizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '50'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion1': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '50'}),
            'logo': forms.FileInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }