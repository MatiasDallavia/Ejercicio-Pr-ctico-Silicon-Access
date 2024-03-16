from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import PrivateAreaSerializer, UserSerializer
from core.permissions import IsPrivateAreaOwner

# Create your views here.


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetToken(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Missing credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class SinglePrivateAreaView(APIView):

    permission_classes = [IsAuthenticated, IsPrivateAreaOwner]

    def delete(self, request, area_pk):
        user = request.user

        private_area = user.privatearea_set.filter(id=area_pk).first()
        if private_area:
            private_area.delete()
            return Response(
                {"status": "successful deletion"}, status=status.HTTP_200_OK
            )
        return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, area_pk):
        user = request.user
        
        private_area = user.privatearea_set.filter(id=area_pk).first()
        if private_area:
            serializer = PrivateAreaSerializer(private_area)
            return Response(serializer.data)
        return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, area_pk):

        user = request.user
        
        private_area = user.privatearea_set.filter(id=area_pk).first()
        if private_area:
            serializer = PrivateAreaSerializer(private_area, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ListPrivateAreaView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        data["user"] = request.user.id

        serializer = PrivateAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        private_areas = user.privatearea_set.all()
        serializer = PrivateAreaSerializer(private_areas, many=True)
        return Response(serializer.data)
