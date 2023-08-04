from django.urls import path
from .views import (
    CompanyCreateAPIView, 
    )

urlpatterns = [
    path('', CompanyCreateAPIView.as_view(), name='company-create'),
]