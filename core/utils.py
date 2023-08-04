import random
import uuid
import string

from equipment import EquipmentCondition, EquipmentStatus, EquipmentType
from equipment.models import Equipment

from company.models import Company, Department
from user.models import User


def generate_guest_email(first_name, last_name):
    return f"{first_name.replace(' ', '_').lower()}{last_name.replace(' ', '_').lower()}@guest.com"

def generate_serial_number():
    random_number = random.randint(1000000, 9999999)
    return random_number

def generate_employee_number():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    return f"{letters}-{numbers}"

def populate_db():
    users = [
        {
            "email": "steve_rogers@avengers.com",
            "first_name": "Steve",
            "last_name": "Rogers",
            "gender": "Male",
            "contact_number": "+639111111111",
            "job_title": "Django Developer"
        },
        {
            "email": "peter_parker@avengers.com",
            "first_name": "Peter",
            "last_name": "Parker",
            "gender": "Male",
            "contact_number": "+639111111112",
            "job_title": "Python Developer"
        },
        {
            "email": "tony_stark@avengers.com",
            "first_name": "Tony",
            "last_name": "Stark",
            "gender": "Male",
            "contact_number": "+639111111113",
            "job_title": "ReactJS Developer"
        },
        {
            "email": "thor_odinson@avengers.com",
            "first_name": "Thor",
            "last_name": "Odinson",
            "gender": "Male",
            "contact_number": "+639111111114",
            "job_title": "ReactNative Developer"
        },
        {
            "email": "natasha_romanoff@avengers.com",
            "first_name": "Natasha",
            "last_name": "Romanoff",
            "gender": "Female",
            "contact_number": "+639111111115",
            "job_title": "DevOps Engineer"
        }
    ]

    companies = [
        {
            "name": "WeARE Solutions, Inc.",
            "description": "Software company"
        },
        {
            "name": "Developers World Inc.",
            "description": "Software company"
        },
        {
            "name": "We Think Soluctions, Co.",
            "description": "Software company"
        }
    ]

    departments = [
        {
            "name": "IT Department",
            "description": "IT Team"
        },
        {
            "name": "HR Department",
            "description": "HR Team"
        },
        {
            "name": "Administration",
            "description": "Admin Department"
        },
        {
            "name": "Finance",
            "description": "Finance Department"
        },
        {
            "name": "Security",
            "description": "Security Detail"
        },
    ]

    for department in departments:
        defaults = {
            "description": department['description']
        }
        department_obj, _ = Department.objects.update_or_create(
            name=department['name'],
            defaults=defaults
        )

    for user in users:
        user_defaults = {
            "first_name": user['first_name'],
            "last_name": user['last_name'],
            "gender": user['gender'],
            "contact_number": user['contact_number'],
            "job_title": user['job_title'],
            "employee_number": generate_employee_number(),
            "department": Department.objects.order_by('?')[0],
            "company": Company.objects.order_by('?')[0]
        }
        user_obj, created = User.objects.update_or_create(
            email=user['email'],
            defaults=user_defaults
        )
        if created:
            user_obj.set_password("Python2023.")
            user_obj.save()

            print("User created: ", user_obj.email)

    
    for company in companies:
        defaults = {
            "description": company['description']
        }
        company_obj, _ = Company.objects.update_or_create(
            name=company['name'],
            defaults=defaults
        )

        print("Company saved. ", company_obj)

def populate_devices():
    devices = [
        {
            "name": "MSI GF77",
            "description": "MSI GF77 Laptop",
            "brand": "MSI",
            "type": EquipmentType.LAPTOP,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.NEW
        },
        {
            "name": "Asus ROG G16",
            "description": "Asus ROG G16 Laptop",
            "brand": "Asus",
            "type": EquipmentType.LAPTOP,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.NEW
        },
        {
            "name": "Apple M2 Pro",
            "description": "Apple M2 Pro Laptop",
            "brand": "Apple",
            "type": EquipmentType.LAPTOP,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.NEW
        },
        {
            "name": "Apple iPad Pro",
            "description": "Apple iPad Pro Tablet",
            "brand": "Apple",
            "type": EquipmentType.TABLET,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.USED
        },
        {
            "name": "Apple iMac Pro",
            "description": "Apple iMac Pro Workstation",
            "brand": "Apple",
            "type": EquipmentType.DESKTOP,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.USED
        },
        {
            "name": "Dell Workstation Pro",
            "description": "Dell Workstation Pro",
            "brand": "Dell",
            "type": EquipmentType.DESKTOP,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.USED
        },
        {
            "name": "iPhone Pro Max 14",
            "description": "iPhone Pro Max 14 Phone",
            "brand": "Apple",
            "type": EquipmentType.MOBILE,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.NEW
        },
        {
            "name": "Samsung S23 Ultra",
            "description": "Samsung S23 Phone",
            "brand": "Samsung",
            "type": EquipmentType.MOBILE,
            "status": EquipmentStatus.UNASSIGNED,
            "condition": EquipmentCondition.NEW
        },
    ]

    for device in devices:
        defaults = {
            "name": device['name'],
            "description": device['description'],
            "brand": device['brand'],
            "type": device['type'],
            "status": device['status'],
            "condition": device['condition']
        }
        equipment_obj, created = Equipment.objects.update_or_create(
            serial_number=generate_serial_number(),
            defaults=defaults
        )

        print("Device saved. ", equipment_obj.name)

