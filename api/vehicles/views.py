from datetime import datetime

from core.permissions import IsPrivateAreaOwner
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class RetrieveCreateVehicleView(APIView):

    permission_classes = [IsAuthenticated, IsPrivateAreaOwner]

    # Retrieves all vehicles for a specific area
    def get(self, request, area_pk):
        request.data["user"] = request.user
        vehicles = Vehicle.objects.filter(private_area__id=area_pk, is_gone=False)

        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Creates a single vehicle for a specific area
    def post(self, request, area_pk):
        request.data["user"] = request.user
        request.data["private_area"] = area_pk
        serializer = VehicleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteVehicleView(APIView):

    permission_classes = [IsAuthenticated, IsPrivateAreaOwner]

    # Retrieves a single vehicle from specified area
    def get(self, request, area_pk, vehicle_pk):

        request.data["user"] = request.user
        vehicle = Vehicle.objects.filter(
            id=vehicle_pk, private_area__id=area_pk, is_gone=False
        ).first()
        if vehicle is None:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Updates a single vehicle from specified area
    def put(self, request, area_pk, vehicle_pk):
        request.data["user"] = request.user
        request.data["private_area"] = area_pk
        vehicle = Vehicle.objects.filter(
            id=vehicle_pk, private_area__id=area_pk, is_gone=False
        ).first()
        serializer = VehicleSerializer(vehicle, request.data)

        if vehicle is None:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Soft-deletes a single vehicle from specified area
    def delete(self, request, area_pk, vehicle_pk):

        vehicle = Vehicle.objects.filter(
            id=vehicle_pk, private_area__id=area_pk, is_gone=False
        ).first()

        if vehicle is None:
            return Response(
                {"status": "vehicle nout found"}, status=status.HTTP_404_BAD_REQUEST
            )

        vehicle.is_gone = True
        vehicle.exit_time = datetime.now()
        vehicle.save()
        return Response({"status": "deleted"}, status=status.HTTP_201_CREATED)
