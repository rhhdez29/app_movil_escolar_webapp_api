from django.db.models import *
from django.db import transaction
from app_movil_escolar_webapp_api.serializers import UserSerializer
from app_movil_escolar_webapp_api.serializers import *
from app_movil_escolar_webapp_api.models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import Group
import json
from django.shortcuts import get_object_or_404
from app_movil_escolar_webapp_api.permissions import IsAdministrador
from rest_framework.permissions import IsAuthenticated

class MateriasAll(generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        materias = Materias.objects.order_by("id")
        lista = MateriaSerializer(materias, many=True).data
        return Response(lista, 200)

class MateriaView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated, IsAdministrador]

    #Obtener usuario por ID
    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, id = request.GET.get("id"))
        materia = MateriaSerializer(materia, many=False).data
        # Si todo es correcto, regresamos la información
        return Response(materia, 200)

    #Registrar una nueva materia
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        #serializamos los datos de la materia para volverla de nuevo a json
        materia = MateriaSerializer(data=request.data)
        print(materia)

        if materia.is_valid(): #Validar los datos
            nrc = request.data['nrc']
            existing_materia = Materias.objects.filter(nrc=nrc)
            if existing_materia:
                return Response({"message":"Materia con NRC "+str(nrc)+", ya existe"},400) #bad request
            materia = Materias.objects.create(
                nrc = nrc,
                nombre_materia = request.data['nombre_materia'],
                seccion = request.data['seccion'],
                dias_json = request.data['dias_json'],
                hora_inicio = request.data['hora_inicio'],
                hora_fin = request.data['hora_fin'],
                salon = request.data['salon'],
                programa_educativo = request.data['programa_educativo'],
                profesor_asignado = request.data['profesor_asignado'],
                creditos = request.data.get('creditos', 0)
            )
            materia.save()

            return Response({"materia_created_id": materia.id}, status=status.HTTP_201_CREATED)

        # Si hay errores de validación del serializer
        return Response(materia.errors, status=status.HTTP_400_BAD_REQUEST)

    # Actualizar datos de la materia
    @transaction.atomic
    def put(self, request, *args, **kwargs):
        # Primero obtenemos la materia a actualizar
        materia = get_object_or_404(Materias, id=request.data["id"])
        materia.nrc = request.data["nrc"]
        materia.nombre_materia = request.data["nombre_materia"]
        materia.seccion = request.data["seccion"]
        materia.dias_json = request.data["dias_json"]
        materia.hora_inicio = request.data["hora_inicio"]
        materia.hora_fin = request.data["hora_fin"]
        materia.salon = request.data["salon"]
        materia.programa_educativo = request.data["programa_educativo"]
        materia.profesor_asignado = request.data["profesor_asignado"]
        materia.creditos = request.data["creditos"]
        materia.save()
        
        return Response({"message": "Materia actualizada correctamente", "Materia": MateriaSerializer(materia).data}, 200)

    # Eliminar maestro con delete (Borrar realmente)
    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, id=request.GET.get("id"))
        try:
            materia.delete()
            return Response({"details":"Materia eliminada"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)