from django.db import models

# Create your models here.

class AFPModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "AFP"
        verbose_name_plural = "AFPs"
        ordering = ["creado"]


class ISAPREModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "ISAPRE"
        verbose_name_plural = "ISAPRES"
        ordering = ["creado"]


class CiudadModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["creado"]

class ArmaServicioModel(models.Model):
    nombre = models.CharField(max_length=100)
    sigla_arma = models.CharField(max_length=100, null=True, blank=True )
    imagen = models.ImageField(upload_to='mantenedor/armas/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Arma y Servicio"
        verbose_name_plural = "Armas y Servicios"
        ordering = ["creado"]

class EstadoCivilModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"
        ordering = ["creado"]

class GradoModel(models.Model):
    grado_sigla = models.CharField(max_length=50)
    grado = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='mantenedor/grado/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grado_sigla

    class Meta:
        verbose_name = "Grado"
        verbose_name_plural = "Grados"
        ordering = ["creado"]

class GrupoSanguineoModel(models.Model):
    nombre = models.CharField(max_length=5)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Grupo Sanguineo"
        verbose_name_plural = "Grupos Sanguineos"
        ordering = ["creado"]

class ProfesionModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "Profesiones"
        ordering = ["creado"]


class ReligionModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religiones"
        ordering = ["creado"]

class UACModel(models.Model):
    uac_sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='mantenedor/uac/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "UAC"
        verbose_name_plural = "UACs"
        ordering = ["creado"]
    

class UBMModel(models.Model):
    ubm_sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    escalon_superior = models.ForeignKey(UACModel, on_delete=models.CASCADE, related_name='ubms')
    imagen = models.ImageField(upload_to='mantenedor/ubm/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "UBM"
        verbose_name_plural = "UBMs"
        ordering = ["creado"]


class ConedecoracionModel(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='mantenedor/condecoracion/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Medalla"
        verbose_name_plural = "Medallas"
        ordering = ["creado"]

class categoriaModel(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["creado"]

class UnidadModel(models.Model):
    unidad_sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100) 
    escalon_superior = models.CharField(max_length=100, null=True, blank=True)   
    imagen = models.ImageField(upload_to='mantenedor/unidad/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
        ordering = ["creado"]