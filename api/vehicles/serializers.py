from rest_framework import serializers

from constants import VEHICLE_TYPES_CHOISES_DICT
from users.models import PrivateArea
from vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "type",
            "owner_id",
            "private_area",
            "color",
            "patent",
            "insurance",
            "expiration_date",
            "entry_time",
            "exit_time",
        ]

    def validate(self, attrs):
        type = attrs.get("type")
        owner_id = attrs.get("owner_id")
        private_area_id = attrs.get("private_area").id
        patent = attrs.get("patent")

        private_area = PrivateArea.objects.filter(id=private_area_id).first()

        if type not in VEHICLE_TYPES_CHOISES_DICT:
            raise serializers.ValidationError(f"'{type}' is not a correct vehicle type")

        if type not in private_area.allowed_vehicles_type:
            raise serializers.ValidationError(
                f"Vehicles of type '{type}' are not allowed in this private area"
            )

        if len(patent) != 7 or not all(True for i in patent if i.isalnum()):
            raise serializers.ValidationError("Patent value has an invalid format")

        if len(str(owner_id)) > 8:
            raise serializers.ValidationError("Owner Id format is invalid")

        return attrs

    def create(self, validated_data):
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle
