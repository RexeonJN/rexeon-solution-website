from django.contrib import admin
from rexeonapp.models import Blog
from rexeonapp.models import Get_in_touch
from rexeonapp.models import Apply

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created_on','status']  
    list_filter = ("status",)
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Blog , BlogAdmin) 

class Get_in_touchAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Contact_no']
admin.site.register(Get_in_touch,Get_in_touchAdmin)

class ApplyAdmin(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Email','Contact_no']
admin.site.register(Apply,ApplyAdmin)
