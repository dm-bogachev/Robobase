from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .forms import EmployeeChangeForm, EmployeeCreationForm

Employee = get_user_model()

class EmployeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm

    list_display = ['username', 'email', 'first_name', 
                    'last_name', 'mid_name', 'position', 
                    'birthday', 'is_staff', 'is_active']
    fieldsets = (
        ('Сведения',
         {'fields': (
         'username', 'password', 'first_name', 
         'last_name', 'mid_name', 'email', 
         'position', 'birthday',)},),

        ('Разрешения',
         {'fields': ('permission_administration', 'permission_accounting', 
                     'permission_service', 'permission_sales',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 
                       'first_name', 'last_name', 'mid_name', 
                       'email', 'position', 'birthday',)},),
        ('Разрешения',
         {'fields': ('permission_administration', 'permission_accounting', 
                     'permission_service', 'permission_sales',)}),
    )

admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Group)