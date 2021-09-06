from django.contrib import admin
from .models import Docter,Department

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class DocterAdmin(admin.ModelAdmin):
    list_display = ['name','qualification','department','queue']
    list_editable = ['queue']

    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Docter,DocterAdmin)