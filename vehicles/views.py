from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from vehicles.serializers import VehicleSerializer


class ListVehicleView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request):
        return Response({})
        data = request.data
        user_id = request.user.id

        # private_area = PrivateArea.objects.filter(user__id=user_id, id=pk).first()
        if private_area:
            private_area.delete()
            return Response(
                {"status": "successful deletion"}, status=status.HTTP_200_OK
            )
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        request.data["user"] = request.user
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        print("DENTRO", pk)
        user_id = request.user.id
        private_area = PrivateArea.objects.filter(user__id=user_id, id=pk).first()
        if private_area:
            serializer = PrivateAreaSerializer(private_area)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        print("DENTRO", pk)
        user_id = request.user.id
        city = request.data.get("city")
        allowed_vehicles_type = request.data.get("allowed_vehicles_type")
        request.data["user"] = user_id

        private_area = PrivateArea.objects.filter(user__id=user_id, id=pk).first()
        if private_area:
            serializer = PrivateAreaSerializer(private_area, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
