from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AFPForm(forms.ModelForm):
    class Meta:
        model = AFPModel
        fields = ['nombre']

class ISAPREForm(forms.ModelForm):
    class Meta:
        model = ISAPREModel
        fields = ['nombre']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = CiudadModel
        fields = ['nombre']

class ArmaServicioForm(forms.ModelForm):
    class Meta:
        model = ArmaServicioModel
        fields = ['nombre', 'sigla_arma','imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        return imagen
    

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivilModel
        fields = ['nombre']

class GradoForm(forms.ModelForm):
    class Meta:
        model = GradoModel
        fields = ['grado_sigla', 'grado', 'imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')        
        return imagen

class GrupoSanguineoForm(forms.ModelForm):
    class Meta:
        model = GrupoSanguineoModel
        fields = ['nombre']

class ProfesionForm(forms.ModelForm):
    class Meta:
        model = ProfesionModel
        fields = ['nombre']

class ReligionForm(forms.ModelForm):
    class Meta:
        model = ReligionModel
        fields = ['nombre']

class UACForm(forms.ModelForm):
    class Meta:
        model = UACModel
        fields = ['uac_sigla', 'nombre', 'imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')        
        return imagen

class UBMForm(forms.ModelForm):
    class Meta:
        model = UBMModel
        fields = ['ubm_sigla', 'nombre', 'escalon_superior', 'imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        return imagen

class CondecoracionForm(forms.ModelForm):
    class Meta:
        model = ConedecoracionModel
        fields = ['nombre', 'imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        return imagen

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoriaModel
        fields = ['nombre']
        
class UnidadForm(forms.ModelForm):
    class Meta:
        model = UnidadModel
        fields = ['unidad_sigla', 'nombre', 'imagen']
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        return imagen
    
    
 