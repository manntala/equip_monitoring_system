from django.urls import path
from .views import (
    CompanyCreateAPIView,
    CompanyCreateEmployee,
    CompanyEmployeeListView,
    CompanyEmployeeDetailView,
    CompanyAssignEquipmentView,
    CompanyReturnEquipmentView,
    DepartmentListView,
    DepartmentCreateView
    )

urlpatterns = [
    path('', CompanyCreateAPIView.as_view(), name='company-create'),
    path('<int:company_id>/create_employee/', CompanyCreateEmployee.as_view(), name='company-create-employee'),
    path('<int:company_id>/employee_list/', CompanyEmployeeListView.as_view(), name='company-employee-list'),
    path('<int:company_id>/employee/<int:id>', CompanyEmployeeDetailView.as_view(), name='company-employee-detail'),

    path('<int:company_id>/employee/<int:employee_id>/assign/', CompanyAssignEquipmentView.as_view(), name='company-assign-equipment'),
    path('<int:company_id>/employee/<int:employee_id>/return/', CompanyReturnEquipmentView.as_view(), name='company-return-equipment'),

    path('department/', DepartmentListView.as_view(), name='department-list'),
    path('department/create/', DepartmentCreateView.as_view(), name='department-create'),

]