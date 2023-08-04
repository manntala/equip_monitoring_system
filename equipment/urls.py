from django.urls import path
from .views import EquipmentListView, EquipmentCreateView, EquipmentFilterView

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment-list-view'),
    path('create/', EquipmentCreateView.as_view(), name='equipment-create-view'),
    path('filter/', EquipmentFilterView.as_view(), name='equipment-filter-view'),
]
