from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from mantenedor.models import UnidadModel, GradoModel
from .models import CustomUser

class CustomLoginForm(forms.Form):
    correo = forms.EmailField(label="Correo", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get("correo")
        password = cleaned_data.get("password")

        from django.contrib.auth import authenticate
        user = authenticate(username=correo, password=password)
        if user is None:
            raise forms.ValidationError("Correo o contraseña incorrectos.")
        cleaned_data['user'] = user
        return cleaned_data


class CustomUserCreationForm(forms.ModelForm):
    correo = forms.EmailField(label="Correo", required=True)
    unidad = forms.ModelChoiceField(queryset=UnidadModel.objects.all(), required=True)
    grado = forms.ModelChoiceField(queryset=GradoModel.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = [
            'correo',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'unidad',
            'grado',
            'foto',
            'citofono',
            'is_admin',
            'is_divper',
            'is_uac',
            'is_ubm',
            'is_lector',
        ]

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get("correo")
        if CustomUser.objects.filter(correo=correo).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return cleaned_data


#Este formulario es para actualizar el usuario, usando el admin
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['password','last_login','is_superuser','first_name','last_name','email','is_staff','is_active','date_joined', 'Groups', 'User permissions'] 

    def save(self, commit=True):
        instance = super().save(commit=False)
        # No modificar contraseña
        if commit:
            instance.save()
        return instance
    

#formulario para editar perfil
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'unidad', 'grado', 'citofono', 'foto']
        widgets = {
            'unidad': forms.Select(attrs={'class': 'form-select'}),
            'grado': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['correo'].widget.attrs['readonly'] = True
    def clean_correo(self):
        return self.instance.correo