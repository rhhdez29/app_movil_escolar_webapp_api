from django.contrib import admin
from django.utils.html import format_html
from app_movil_escolar_webapp_api.models import *


@admin.register(Administradores)
@admin.register(Alumnos)
@admin.register(Maestros)

#TODO: Aqui agregar el de estudiantes y profesores

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

