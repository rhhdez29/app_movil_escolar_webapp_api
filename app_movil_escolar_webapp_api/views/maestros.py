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

class MaestrosAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = request.user
        #TODO: Regresar perfil del usuario
        return Response({})

class MaestroView(generics.CreateAPIView):

    #Registrar un nuevo usuario
    @transaction.atomic
    def post(self, request, *args, **kwargs):

        #serializamos los datos del administrador para volverlo de nuevo a json
        user = UserSerializer(data=request.data)

        if user.is_valid():
            #Grab user data
            role = request.data['rol']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']
            #Valida si existe el usuario o bien el email registrado
            existing_user = User.objects.filter(email=email).first()

            if existing_user:
                return Response({"message":"Username "+email+", is already taken"},400) #bad request 

            user = User.objects.create( username = email,
                                        email = email,
                                        first_name = first_name,
                                        last_name = last_name,
                                        is_active = 1)


            user.save()
            #Encriptamos la contraseña
            user.set_password(password)
            user.save()

            group, created = Group.objects.get_or_create(name=role)
            group.user_set.add(user)
            user.save()

            #Almacenar los datos adicionales del administrador
            maestro = Maestros.objects.create(
                user = user,
                id_trabajador = request.data['id_trabajador'],
                telefono = request.data['telefono'],
                fecha_nacimiento = request.data['fecha_nacimiento'],
                rfc = request.data['rfc'].upper(),
                cubiculo = request.data['cubiculo'],
                area_investigacion = request.data['area_investigacion'],
                materias_json = request.data['materias_json']
            )
            maestro.save()

            return Response({"maestro_created_id": maestro.id}, 201)

        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
