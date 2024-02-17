from django.contrib import admin
from .models import Projects,Category,Service
# Register your models here.
admin.site.register(Projects)

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Category,CatagoryAdmin) 

admin.site.register(Service)