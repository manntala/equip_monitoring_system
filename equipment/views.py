from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from equipment.models import Equipment

from equipment.serializers import EquipmentSerializer


class EquipmentCreateView(CreateAPIView):
    serializer_class = EquipmentSerializer
    

class EquipmentListView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentFilterView(ListAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()

        equipment_type = self.request.query_params.get('type')
        equipment_status = self.request.query_params.get('status')
        equipment_condition = self.request.query_params.get('condition')

        if equipment_type:
            equipment_type = equipment_type.lower()
            queryset = queryset.filter(type__iexact=equipment_type)

        if equipment_status:
            equipment_status = equipment_status.lower()
            queryset = queryset.filter(status__iexact=equipment_status)

        if equipment_condition:
            equipment_condition = equipment_condition.lower()
            queryset = queryset.filter(condition__iexact=equipment_condition)

        return queryset