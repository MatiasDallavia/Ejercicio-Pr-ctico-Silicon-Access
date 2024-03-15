from django.db import models


# Create your models here.
class Vehicle(models.Model):

    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"
    TRUCK = "TRUCK"
    SAILBOAT = "SAILBOAT"
    BOAT = "BOAT"

    VEHICLE_TYPES_CHOISES = (
        (CAR, "Car"),
        (MOTORCYCLE, "MOTORCYCLE"),
        (TRUCK, "TRUCK"),
        (SAILBOAT, "SAILBOAT"),
        (BOAT, "BOAT"),
    )

    type = models.CharField(
        choices=VEHICLE_TYPES_CHOISES, max_length=25, default="CAR", null=False
    )
    owner_id = models.IntegerField(null=False)
    color = models.CharField(max_length=25, null=False)
    patent = models.CharField(max_length=7, null=False)
    insurance = models.CharField(max_length=7, null=False)
    expiration_date = models.DateField(null=False)
    entry_time = models.DateTimeField(auto_now_add=True, null=False)
    exit_time = models.DateTimeField(null=True)
    is_gone = models.BooleanField(default=False)
