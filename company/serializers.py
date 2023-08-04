from rest_framework import serializers

from user.models import User
from .models import Company, Department

from equipment.serializers import EquipmentSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'password',
            'employee_number',
            'job_title',
            'department',
            'company'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserEmployeeSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'contact_number',
            'employee_number',
            'job_title',
            'department',
            'company',
            'equipment'
        ]


class EmployeeDetailSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'contact_number',
            'employee_number',
            'job_title',
            'department',
            'company',
            'equipment'
        ] 


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'