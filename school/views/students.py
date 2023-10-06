from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from school.models import Student
from school.serializers import StudentSerialize


class StudentsViewSet(viewsets.ModelViewSet):
    """ Display all students """
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
