from django.contrib import admin
from  fristapp.models import student,usercreation
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display =['name','age','phone','address','pic','st_id']

class usercreationadmin(admin.ModelAdmin):
    list_display =['user_name','user_email','user_pic']

admin.site.register(student,studentadmin)
admin.site.register(usercreation,usercreationadmin)
