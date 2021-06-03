# snippets/serializers
from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = (
            'id',
            'descripcion',
            'duracion',
            'tiempo_registrado',
            'estatus',
            'creado_a',
            'actualizado_a',
        )