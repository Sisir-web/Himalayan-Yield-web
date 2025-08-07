from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser

    fieldsets = (
        ('data', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'age', 'phone', 'country', 'state', 'city', 'pincode', 'local_address', 'gender', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_admin' ,'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'name', 'is_admin', 'is_superuser')
    list_filter = ('is_admin', 'is_superuser', 'is_active')

    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(MyUser, MyUserAdmin)
