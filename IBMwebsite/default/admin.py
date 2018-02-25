from django.contrib import admin
from default.models import RegisterTable


# Register your models here.

class RegisterTable_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'name','time' )

admin.site.register(RegisterTable,RegisterTable_ModelAdmin)
