from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from company.factories import CompanyFactory, DepartmentFactory

from user.models import User
from .models import Company
from .serializers import CompanyCreateEmployeeSerializer, CompanySerializer, UserEmployeeSerializer


class CompanyAPIViewTest(APITestCase):
    def setUp(self):
        self.department = DepartmentFactory.create()
        self.company = CompanyFactory.create()

        self.user1 = User.objects.create(first_name='John', last_name='Doe', company=self.company, email='john_doe@email.com')
        self.user2 = User.objects.create(first_name='Jane', last_name='Smith', company=self.company, email='jane_smith@email.com')

    def test_create_company(self):
        url = reverse('company-create')
        data = {
            'name': 'Test Company',
            'location': 'Test Location',
            'description': 'Test Description',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.all().last()
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)

    def test_create_company_invalid_data(self):
        url = reverse('company-create')
        data = {
            # missing data
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)