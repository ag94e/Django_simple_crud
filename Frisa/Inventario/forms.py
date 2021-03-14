from django import forms
from .models import ModeloInventario

class FormularioInventario(forms.ModelForm):
    
    class Meta:
        model = ModeloInventario
        fields = [
            'codigo',
            'cantidad',
            'unidad_medida',
            'clase_valoracion',
            'descripcion',
            'ubicacion',
            'almacen',
            'modelo',
            'marca',
        ]
        labels = {
            'codigo': 'Código',
            'cantidad': 'Cantidad',
            'unidad_medida': 'Unidad de medida',
            'clase_valoracion': 'Clase de valoración',
            'descripcion': 'Descripción',
            'ubicacion': 'Ubicación',
            'almacen': 'Almacén',
            'modelo': 'Modelo',
            'marca': 'Marca',
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'clase_valoracion': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'almacen': forms.Select(attrs={'class': 'form-control'}), 
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
        }