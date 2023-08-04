from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from user.models import User

from .serializers import CompanyCreateEmployeeSerializer, CompanySerializer, EmployeeDetailSerializer, UserEmployeeSerializer

from .models import Company


class CompanyCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyCreateEmployee(APIView):
    def post(self, request, company_id, format=None):
        data = request.data.copy()
        data['password'] = make_password(data['password'])

        company = get_object_or_404(Company, id=company_id)
        data['company'] = company.id

        serializer = CompanyCreateEmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
