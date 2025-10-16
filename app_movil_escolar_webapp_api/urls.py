from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views.bootstrap import VersionView
from app_movil_escolar_webapp_api.views import bootstrap
from app_movil_escolar_webapp_api.views import users
from app_movil_escolar_webapp_api.views import auth
#from app_movil_escolar_webapp_api.views import alumnos
#from app_movil_escolar_webapp_api.views import profesores

urlpatterns = [
    
    #Create admin
    path('admin/', users.AdminView.as_view()),
    #Admin data
    path('list/admin', users.AdminAll.as_view()),
    #Edit admin
    #path('admins-edit/', users.AdminsViewEdit.as_view()),

    path('alumno/', users.AlumnoView.as_view()),
    path('list/alumnos', users.AlumnosAll.as_view()),

    path('maestro/', users.MaestroView.as_view()),
    path('list/maestros', users.MaestrosAll.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
