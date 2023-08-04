from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from user.models import User

from .serializers import CompanyCreateEmployeeSerializer, CompanySerializer, EmployeeDetailSerializer, UserEmployeeSerializer

from .models import Company


class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanySerializer


class CompanyCreateEmployee(CreateAPIView):
    def create(self, request, company_id, *args, **kwargs):
        data = request.data.copy()
        data['password'] = make_password(data['password'])

        company = get_object_or_404(Company, id=company_id)
        data['company'] = company.id

        serializer = CompanyCreateEmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CompanyEmployeeListView(ListAPIView):
    serializer_class = UserEmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = User.objects.filter(company__id=company_id)

        return queryset
    

class CompanyEmployeeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        employee_id = self.kwargs.get('id')

        queryset = User.objects.filter(id=employee_id, company__id=company_id)

        return queryset
