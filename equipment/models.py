from django.db import models
from model_utils.models import TimeStampedModel

from equipment import EquipmentCondition, EquipmentStatus, EquipmentType

class Equipment(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=30)
    type = models.CharField(choices=EquipmentType.CHOICES, max_length=20)
    status = models.CharField(choices=EquipmentStatus.CHOICES, default=EquipmentStatus.UNASSIGNED, max_length=20)
    condition = models.CharField(choices=EquipmentCondition.CHOICES, default=EquipmentCondition.NEW, max_length=20)

    def __str__(self) -> str:
        return self.name