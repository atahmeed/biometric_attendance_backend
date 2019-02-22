from attendanceSystem.api.views import StudentViewSet,AttendanceViewSet
from rest_framework.routers import SimpleRouter,DefaultRouter

router = SimpleRouter()
router.register(r'student', StudentViewSet, base_name='students')
router.register(r'attendance', AttendanceViewSet, base_name='attendance')

urlpatterns = router.urls