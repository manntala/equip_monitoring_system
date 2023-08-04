import factory
from factory.fuzzy import FuzzyChoice
from django.utils.text import slugify
from django.core.files import File
from faker import Faker

from company.models import Company, Department


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = FuzzyChoice(choices=['SkyLink Co.', 'StarLink Inc.', 'SkyNet Co.'])
    description = "This is a sample description of the company"

class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = FuzzyChoice(choices=['IT Team', 'HR Department', 'Finance', 'Administration'])
    description = "This is the description for this department"


