from django.contrib import admin
from .models import *

class MaterialInline(admin.TabularInline):
    model = Material
    fields = ['tipoMaterial','autor','titulo','año','status']

class PersonaInline(admin.TabularInline):
    model = Persona
    fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [MaterialInline, PersonaInline]

# Register your models here.

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Material)
admin.site.register(Libro)
admin.site.register(Revista)