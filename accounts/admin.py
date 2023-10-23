from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'department', 'password')})
UserAdmin.fieldsets = tuple(fields)
UserAdmin.list_display = ('username', 'department', 'is_staff', 'last_login')

admin.site.register(CustomUser, UserAdmin)
