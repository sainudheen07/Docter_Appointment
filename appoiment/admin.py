from django.contrib import admin
from .models import PatientDetail

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    admin.site.register(PatientDetail)