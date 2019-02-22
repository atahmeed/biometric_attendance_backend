from rest_framework import serializers
from attendanceSystem.models import Student, Attendance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'roll','present')
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('roll', 'date','time')
        read_only_fields=('date','time')