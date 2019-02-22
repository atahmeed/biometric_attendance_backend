from django.contrib import admin
from .models import Student,Attendance
from django.core.exceptions import NON_FIELD_ERRORS
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll','name','present')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('roll','date','time')

admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)