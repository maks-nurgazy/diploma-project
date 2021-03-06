from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import gettext as _

from users.models import User, Teacher, Student


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'get_roles']

    def get_roles(self, user):
        return [role.get_id_display() for role in user.roles.all()]

    get_roles.short_description = 'Roles'
    get_roles.admin_order_field = 'id'

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser')}
         ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    )


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Student)
class StudentAdmin(UserAdmin):
    def save_related(self, request, form, formsets, change):
        super(StudentAdmin, self).save_related(request, form, formsets, change)
        form.instance.roles.add(4)


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    def save_related(self, request, form, formsets, change):
        super(TeacherAdmin, self).save_related(request, form, formsets, change)
        form.instance.roles.add(3)
