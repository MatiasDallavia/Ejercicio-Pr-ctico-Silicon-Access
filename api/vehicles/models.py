from django.db import models

from constants import VEHICLE_TYPES_CHOISES
from users.models import PrivateArea


class Vehicle(models.Model):

    type = models.CharField(
        choices=VEHICLE_TYPES_CHOISES, max_length=25, default="CAR", null=False
    )
    private_area = models.ForeignKey(
        PrivateArea, null=False, on_delete=models.DO_NOTHING
    )
    driver_name = models.CharField(max_length=35)
    color = models.CharField(max_length=35, null=False)
    patent = models.CharField(max_length=7, null=False)
    insurance = models.CharField(max_length=35, null=False)
    expiration_date = models.DateField(null=False)
    entry_time = models.DateTimeField(auto_now_add=True, null=False)
    exit_time = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)
