from django.db import models
from mantenedor.models import ConedecoracionModel, GradoModel, ArmaServicioModel
from reservistas.models import ReservistaModel



# Create your models here.

class ResolucionMedalla(models.Model):
    fecha_resolucion = models.DateField()
    numero_resolucion = models.CharField(max_length=100)
    fecha_otorgamiento = models.DateField()
    tipo_medalla = models.ForeignKey(ConedecoracionModel, on_delete=models.CASCADE)
    id_reservista = models.ForeignKey(ReservistaModel, on_delete=models.CASCADE)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resolución {self.numero_resolucion} - {self.tipo_medalla.nombre}"

    class Meta:
        verbose_name = "Resolución de Medalla"
        verbose_name_plural = "Resoluciones de Medallas"
        ordering = ["fecha_resolucion"]

class ResolucionAscenso(models.Model):
    TIPO_RESOLUCION_CHOICES = [
        ('Ascenso', 'Ascenso'),
        ('Nombramiento', 'Nombramiento'),
    ]

    fecha_resolucion = models.DateField()
    numero_resolucion = models.CharField(max_length=100)
    fecha_ascenso = models.DateField()
    tipo_resolucion = models.CharField(max_length=20, choices=TIPO_RESOLUCION_CHOICES)
    resolucion = models.FileField(upload_to='resoluciones_ascenso/', null=True, blank=True)
    id_reservista = models.ForeignKey(ReservistaModel, on_delete=models.CASCADE)
    grado = models.ForeignKey(GradoModel, on_delete=models.CASCADE, default=1) 

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resolución {self.numero_resolucion} - {self.tipo_resolucion}"

    class Meta:
        verbose_name = "Resolución de Ascenso"
        verbose_name_plural = "Resoluciones de Ascensos"
        ordering = ["fecha_resolucion"]
   
class ResolucionCambioEscalafon(models.Model):   
    fecha_resolucion = models.DateField()
    numero_resolucion = models.CharField(max_length=100)
    id_reservista = models.ForeignKey(ReservistaModel, on_delete=models.CASCADE)
    grado = models.ForeignKey(GradoModel, on_delete=models.CASCADE)
    Escalafon_proveniente = models.ForeignKey(
        ArmaServicioModel, 
        on_delete=models.CASCADE,
        related_name='Escalafon_proveniente'
    )
    Escalafon_destino = models.ForeignKey(
        ArmaServicioModel, 
        on_delete=models.CASCADE,
        related_name='escalafon_destino',
        default=10
    )
    resolucion = models.FileField(upload_to='resoluciones_escalafon/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resolución {self.numero_resolucion} - {self.fecha_resolucion}"

    class Meta:
        verbose_name = "Cambio de Escalafón"
        verbose_name_plural = "Cambios de Escalafones"
        ordering = ["fecha_resolucion"]

class ResolucionCambioInstitucion(models.Model):
    PROCEDENCIA_CHOICES = [
        ('Ejercito', 'Ejercito'),
        ('Armada', 'Armada'),
        ('Fuerza Aerea', 'Fuerza Aerea'),
    ]
    
    fecha_resolucion = models.DateField()
    numero_resolucion = models.CharField(max_length=100)
    id_reservista = models.ForeignKey(ReservistaModel, on_delete=models.CASCADE)
    grado = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=50, choices=PROCEDENCIA_CHOICES)
    destino = models.CharField(max_length=50, choices=PROCEDENCIA_CHOICES)
    resolucion = models.FileField(upload_to='resoluciones_institucion/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resolución {self.numero_resolucion} - {self.fecha_resolucion}"

    class Meta:
        verbose_name = "Cambio de institucion"
        verbose_name_plural = "Cambios de instituciones"
        ordering = ["fecha_resolucion"]