from django.contrib import admin
from .models import *

class MaterialInline(admin.TabularInline):
    model = Material
    fields = ['tipoMaterial','autor','titulo','año','status']
    extra = 0

    

class PersonaInline(admin.TabularInline):
    model = Persona
    fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [MaterialInline, PersonaInline]
   
class LibroAdmin(admin.ModelAdmin): 
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status','editorial',]
   
class RevistaAdmin(admin.ModelAdmin): 
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status',]

class AlumnoAdmin(admin.ModelAdmin): 
    list_display = ['matricula','tipoPersona','nombre','apellido','correo','telefono','numLibros', 'adeudo',]

class ProfesorAdmin(admin.ModelAdmin): 
    list_display = ['numEmpleado', 'tipoPersona', 'nombre', 'apellido', 'correo', 'telefono', 'numLibros', 'adeudo',]
   



# Register your models here.

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Material)
admin.site.register(Libro)
admin.site.register(Revista)