from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from equipment import EquipmentStatus
from equipment.models import Equipment

from user.models import User

from .serializers import CompanyCreateEmployeeSerializer, CompanySerializer, DepartmentSerializer, EmployeeDetailSerializer, UserEmployeeSerializer

from .models import Company, Department


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
    

class CompanyAssignEquipmentView(APIView):
    def post(self, request, company_id, employee_id, *args, **kwargs):
        try:
            company = get_object_or_404(Company, id=company_id)
            user = User.objects.get(company=company, id=employee_id)
        except User.DoesNotExist:
            return Response(f"User not found with an id {employee_id} in this company.", status=404)

        equipment_ids = request.data.get('equipment', [])

        assigned_equipment = Equipment.objects.filter(id__in=equipment_ids, status=EquipmentStatus.ASSIGNED)
        if assigned_equipment.exists():
            return Response("Cannot assign already assigned equipment.", status=400)

        equipment = Equipment.objects.filter(id__in=equipment_ids)

        user.equipment.add(*equipment)

        equipment.update(status=EquipmentStatus.ASSIGNED)

        user_serializer = UserEmployeeSerializer(user)

        response_data = {
            'user': user_serializer.data,
        }

        return Response(response_data, status=200)
    

class CompanyReturnEquipmentView(APIView):
    def post(self, request, company_id, employee_id, *args, **kwargs):
        try:
            company = get_object_or_404(Company, id=company_id)
            user = User.objects.get(company=company, id=employee_id)
        except User.DoesNotExist:
            return Response(f"User not found with an id {employee_id} in this company.", status=404)

        equipment_ids = request.data.get('equipment', [])

        assigned_equipment = Equipment.objects.filter(id__in=equipment_ids)
        if not assigned_equipment.exists():
            return Response("Equipment not assigned.", status=400)

        equipment = Equipment.objects.filter(id__in=equipment_ids)

        user.equipment.remove(*equipment)

        equipment.update(status=EquipmentStatus.UNASSIGNED)

        user_serializer = UserEmployeeSerializer(user)

        response_data = {
            'user': user_serializer.data,
        }

        return Response(response_data, status=200)
    

class DepartmentCreateView(CreateAPIView):
    serializer_class = DepartmentSerializer


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all().order_by('-created')

