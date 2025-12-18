from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from mantenedor.models import  GradoModel, UnidadModel

class CustomUser(AbstractUser):
    username = None  # Elimina el campo username

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)    
    unidad = models.ForeignKey(UnidadModel, on_delete=models.CASCADE, null=True)
    grado = models.ForeignKey(GradoModel, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='core/usuario/', blank=True, null=True)
    citofono = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False)
    is_divper = models.BooleanField(default=False)
    is_uac = models.BooleanField(default=False)
    is_ubm = models.BooleanField(default=False)
    is_lector = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno']
    
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.email = self.correo 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.grado} - {self.nombre} {self.apellido_paterno}"
    
    
