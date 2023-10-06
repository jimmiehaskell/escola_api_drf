from django.contrib import admin
from school.models import Course, Registration, Student


# Customize your admin templates here.
class CousesModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'course_code',
        'description',
    )
    list_display_links = (
        'id',
        'course_code',
    )
    search_fields = (
        'course_code',
    )
    list_per_page = 20


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'course_period',
    )
    list_display_links = (
        'id',
    )
    list_per_page = 20


class StudentsModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'personal_id',
        'cpf',
        'date_of_birth',
    )
    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    list_per_page = 20


# Register your models here.
admin.site.register(Course, CousesModelAdmin)
admin.site.register(Registration, RegistrationModelAdmin)
admin.site.register(Student, StudentsModelAdmin)
