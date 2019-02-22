from rest_framework import viewsets
from attendanceSystem.models import Student,Attendance
from .serializers import StudentSerializer,AttendanceSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()