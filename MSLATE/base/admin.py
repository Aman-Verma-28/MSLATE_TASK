from django.contrib import admin
from .models import UserDetails, NewUserDetails
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class StudentResource(resources.ModelResource):
   class Meta:
      model = UserDetails

class StudentResource2(resources.ModelResource):
   class Meta:
      model = NewUserDetails


class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

class StudentAdmin2(ImportExportModelAdmin):
   resource_class = StudentResource2

admin.site.register(UserDetails, StudentAdmin)
admin.site.register(NewUserDetails, StudentAdmin2)

