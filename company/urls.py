from django.urls import path
from .views import (
    CompanyCreateAPIView,
    CompanyCreateEmployee,
    CompanyEmployeeListView,
    CompanyEmployeeDetailView,
    )

urlpatterns = [
    path('', CompanyCreateAPIView.as_view(), name='company-create'),
    path('<int:company_id>/create_employee/', CompanyCreateEmployee.as_view(), name='company-create-employee'),
    path('<int:company_id>/employee_list/', CompanyEmployeeListView.as_view(), name='company-employee-list'),
    path('<int:company_id>/employee/<int:id>', CompanyEmployeeDetailView.as_view(), name='company-employee-detail'),
]