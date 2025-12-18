from django.db import models
from datetime import date
from mantenedor.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.

class ReservistaModel(models.Model):
    TIPO_ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Retiro Temporal', 'Retiro Temporal'),
    ]
    TIPO_GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Prefiero no decirlo', 'Prefiero no decirlo'),
    ]


    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    run = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=50, choices=TIPO_GENERO_CHOICES)
    grado = models.ForeignKey('mantenedor.GradoModel', on_delete=models.CASCADE)
    ciudad = models.ForeignKey('mantenedor.CiudadModel', on_delete=models.CASCADE, null=True, blank=True)
    isapre = models.ForeignKey('mantenedor.ISAPREModel', on_delete=models.CASCADE, null=True, blank=True)
    afp = models.ForeignKey('mantenedor.AFPModel', on_delete=models.CASCADE, null=True, blank=True)
    estado_civil = models.ForeignKey('mantenedor.EstadoCivilModel', on_delete=models.CASCADE, null=True, blank=True)
    grupo_sanguineo = models.ForeignKey('mantenedor.GrupoSanguineoModel', on_delete=models.CASCADE, null=True, blank=True)
    religion = models.ForeignKey('mantenedor.ReligionModel', on_delete=models.CASCADE, null=True, blank=True)
    arma = models.ForeignKey('mantenedor.ArmaServicioModel', on_delete=models.CASCADE, null=True, blank=True)
    profesion = models.ForeignKey('mantenedor.ProfesionModel', on_delete=models.CASCADE, null=True, blank=True)
    ubm = models.ForeignKey('mantenedor.UBMModel', on_delete=models.CASCADE)
    uac = models.ForeignKey('mantenedor.UACModel', on_delete=models.CASCADE)
    categoria = models.ForeignKey("mantenedor.categoriaModel", on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=TIPO_ESTADO_CHOICES)
    foto = models.ImageField(upload_to='gestion_reserva/reservistas/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    @property
    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
        
    def clean(self):
        super().clean()
        # Validar longitud de 'run' (debe tener 7 dígitos)
        if len(str(self.run)) < 7:
            raise ValidationError(_('El RUN debe contener mínimo 7 dígitos.'))
        
        # Validar longitud de 'dv' (debe tener 1 carácter)
        if len(self.dv) != 1:
            raise ValidationError(_('El DV debe tener exactamente 1 carácter.'))

    def __str__(self):
        return f"{self.grado} - {self.nombre} {self.apellido_paterno} {self.apellido_materno} "

    class Meta:
        verbose_name = "Reservista"
        verbose_name_plural = "Reservistas"
        ordering = ["creado"]
