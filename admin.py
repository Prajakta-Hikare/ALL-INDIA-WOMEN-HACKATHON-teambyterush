from django.contrib import admin
from .models import Patient

# Register the Patient model to make it accessible in the admin interface.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('Hospital_Name', 'Address', 'Speciality', 'Contact', 'Intro','Email')
    list_filter = ('sex',)
    search_fields = ('name',)


# Register your models here.
