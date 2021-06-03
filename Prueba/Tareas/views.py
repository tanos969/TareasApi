from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Tarea
from .serializers import TareaSerializer

from datetime import datetime, timezone


@api_view(['GET', 'POST', 'DELETE'])
def tarea_list(request):

    if request.method == 'GET':
        #traer todas las tareas
        tarea = Tarea.objects.all()

        tareas_serializer = TareaSerializer(tarea, many=True)
        return JsonResponse(tareas_serializer.data, safe=False)

    elif request.method == 'POST':
        #crear una nueva tarea
        tarea_data = JSONParser().parse(request)
        tarea_serializer = TareaSerializer(data=tarea_data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse(tarea_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(tarea_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    #borrar muchas tareas
    elif request.method == 'DELETE':
        return JsonResponse({'message': 'Metodo no encontrado'},
                            status=status.HTTP_400_NOT_FOUND)


@api_view(['GET'])
def completar_tarea(request, pk):
    #validar si existe el objecto
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return JsonResponse({'message': 'La tarea no existe'},
                            status=status.HTTP_404_NOT_FOUND)

    if tarea.estatus == True:
        return JsonResponse({'message': 'La tarea ya fue finalizada'},
                            status=status.HTTP_400_BAD_REQUEST)
    #regresa la tarea completada
    if request.method == 'GET':
        tarea.estatus = True
        tarea.actualizado_a = datetime.now(timezone.utc)
        minutos = (tarea.actualizado_a - tarea.creado_a).total_seconds() / 60
        tarea.tiempo_registrado = minutos
        tarea.save()
        tarea_serializer = TareaSerializer(tarea)
        return JsonResponse(tarea_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def tarea_detail(request, pk):
    # traer por medio del pk (id) una tarea

    #validar si existe el objecto
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return JsonResponse({'message': 'La tarea no existe'},
                            status=status.HTTP_404_NOT_FOUND)

    #traer una tarea
    if request.method == 'GET':
        tarea_serializer = TareaSerializer(tarea)
        return JsonResponse(tarea_serializer.data)

    #actualizar una tarea
    elif request.method == 'PUT':
        tarea_data = JSONParser().parse(request)
        tarea_serializer = TareaSerializer(tarea, data=tarea_data)
        if tarea.estatus == True:
            return JsonResponse({'message': 'La tarea ya fue finalizada'},
                                status=status.HTTP_400_BAD_REQUEST)

        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse(tarea_serializer.data)
        return JsonResponse(tarea_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    #borrar una tarea
    elif request.method == 'DELETE':

        tarea.delete()
        return JsonResponse({'message': 'La tarea fue borrada'},
                            status=status.HTTP_204_NO_CONTENT)
