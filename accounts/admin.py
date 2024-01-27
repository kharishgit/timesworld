from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email','username','role','is_active')
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,CustomUserAdmin)
# admin.site.register(UserProfile)