from django.urls import include, path
from rest_framework import routers
from school.views import CoursesViewSet, ListStudentEnrolledCourse, RegistrationsViewSet, StudentsViewSet, StudentEnrollmentList

router = routers.DefaultRouter()
router.register('courses', CoursesViewSet, basename='courses')
router.register('registrations', RegistrationsViewSet, basename='registrations')
router.register('students', StudentsViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', StudentEnrollmentList.as_view()),
    path('courses/<int:pk>/registrations/', ListStudentEnrolledCourse.as_view()),
]
