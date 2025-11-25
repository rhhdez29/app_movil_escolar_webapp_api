from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views.bootstrap import VersionView
from app_movil_escolar_webapp_api.views import bootstrap
from app_movil_escolar_webapp_api.views import users
from app_movil_escolar_webapp_api.views import alumnos
from app_movil_escolar_webapp_api.views import maestros
from app_movil_escolar_webapp_api.views import materias
from app_movil_escolar_webapp_api.views import auth

urlpatterns = [
    
    #Create admin
    path('admin/', users.AdminView.as_view()),
    #Admin data
    path('lista-admins/', users.AdminAll.as_view()),
    #Edit admin
    #path('admins-edit/', users.AdminsViewEdit.as_view()),

    path('alumnos/', alumnos.AlumnoView.as_view()),
    path('lista-alumnos/', alumnos.AlumnosAll.as_view()),

    path('maestros/', maestros.MaestroView.as_view()),

    path('lista-maestros/', maestros.MaestrosAll.as_view()),

    path('materias/', materias.MateriaView.as_view()),

    path('lista-materias/', materias.MateriasAll.as_view()),

    #Total users
    path('total-usuarios/', users.TotalUsers.as_view()),

    #Login
    path('login/', auth.CustomAuthToken.as_view()),
    #Logout
    path('logout/', auth.Logout.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
