from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver


class Tarea(models.Model):
    """
    modelo que representa una tarea
    """

    descripcion = models.CharField(max_length=200)
    duracion = models.IntegerField()
    tiempo_registrado = models.IntegerField(blank=True, null=True)
    estatus = models.BooleanField(default=False, blank=True)
    creado_a = models.DateTimeField(auto_now_add=True, blank=True)
    actualizado_a = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion