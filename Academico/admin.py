from django.contrib import admin
from .models import Curso

# Register your models here.
admin.site.register(Curso) #Registramos el modelo para poder utilizarlo en el sitio / admin
