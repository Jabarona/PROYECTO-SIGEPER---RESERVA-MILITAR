from django import forms
from .models import *

class ResolucionMedallaForm(forms.ModelForm):
    class Meta:
        model = ResolucionMedalla
        fields = [
            'fecha_resolucion', 
            'numero_resolucion', 
            'fecha_otorgamiento', 
            'tipo_medalla', 
            'id_reservista'
        ]
        widgets = {
            'fecha_resolucion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_otorgamiento': forms.DateInput(attrs={'type': 'date'}),
        }

class ResolucionAscensoForm(forms.ModelForm):
    class Meta:
        model = ResolucionAscenso
        fields = [
            'fecha_resolucion', 
            'numero_resolucion', 
            'fecha_ascenso', 
            'tipo_resolucion', 
            'resolucion', 
            'id_reservista', 
            'grado'
        ]
        widgets = {
            'fecha_resolucion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ascenso': forms.DateInput(attrs={'type': 'date'}),
        }

class ResolucionCambioEscalafonForm(forms.ModelForm):
    class Meta:
        model = ResolucionCambioEscalafon
        fields = [
            'fecha_resolucion', 
            'numero_resolucion', 
            'id_reservista', 
            'grado', 
            'Escalafon_proveniente', 
            'Escalafon_destino', 
            'resolucion'
        ]
        widgets = {
            'fecha_resolucion': forms.DateInput(attrs={'type': 'date'}),
        }

class ResolucionCambioInstitucionForm(forms.ModelForm):
    class Meta:
        model = ResolucionCambioInstitucion
        fields = [
            'fecha_resolucion', 
            'numero_resolucion', 
            'id_reservista', 
            'grado', 
            'procedencia', 
            'destino', 
            'resolucion'
        ]
        widgets = {
            'fecha_resolucion': forms.DateInput(attrs={'type': 'date'}),
        }