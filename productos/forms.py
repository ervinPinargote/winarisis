from django import forms

from .models import producto, presentacion, calificacion


class AgregarProductosForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = [
            'nombre_producto',
            'desc_beneficio',
            'fecha_registro',
            'id_organizacion',
        ]
        labels = {
            'nombre_producto': 'Nombre',
            'desc_beneficio': 'Beneficios',
            'fecha_registro': 'Fecha',
            'id_organizacion': 'Organizacion',
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'desc_beneficio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control'}),
            'id_organizacion': forms.Select(attrs={'class': 'form-control'}),
        }


class AgregarPresentacionesProductosForm(forms.ModelForm):
    class Meta:
        model = presentacion
        fields = [
            'nombre_presentacion',
            'logo',
            'detalles',
            'estado',
            'cont_neto',
            'precio',
            'precio_mayor',
            'id_unidad_medida',
            'id_categoria',
            'id_producto',
        ]
        labels = {
            'nombre_presentacion': 'Nombre Presentacion',
            'logo': 'Logo Presentacion',
            'detalles': 'Detalles',
            'estado': 'Estado',
            'cont_neto': 'Contenido Neto',
            'precio': 'Precio Normal',
            'precio_mayor': 'Precio Por Mayor',
            'id_unidad_medida': 'Unidades de Medida',
            'id_categoria': 'Categoria de la Presentacion',
            'id_producto': 'Producto Base',
        }
        widgets = {
            'nombre_presentacion': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'detalles': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'cont_neto': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_mayor': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'id_producto': forms.Select(attrs={'class': 'form-control'}),

        }


class CalificarProductosForm(forms.ModelForm):
    class Meta:
        model = calificacion
        fields = [
            'comentario',
            'fecha_registro',
            'porcentaje',
            'id_usuario',
            'id_presentacion',
        ]
        labels = {
            'comentario': 'Comentario',
            'fecha_registro': 'Fecha de Registro',
            'porcentaje': 'Calificacion',
            'id_usuario': 'Usuario logeado',
            'id_presentacion': 'Producto Seleccionado',
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control'}),
            'porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
            'id_presentacion': forms.Select(attrs={'class': 'form-control'}),
        }
