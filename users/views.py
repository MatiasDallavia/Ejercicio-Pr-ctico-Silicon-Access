from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer, PrivateAreaSerializer
from users.models import PrivateArea
# Create your views here.


class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not all(
            [bool(i) for i in [username, password, email, last_name, first_name]]
        ):
            return Response(
                {"error": "Missing credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
        
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

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id

        allowed_vehicles_type = request.data.get("allowed_vehicles_type")
        city = request.data.get("city")

        if not city or not allowed_vehicles_type:
            return Response(
                {"error": "Missing credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PrivateAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request):
        data = request.data
        user_id = request.user.id
        private_area = PrivateArea.objects.filter(user__id=user_id)
        if private_area:
            serializer = PrivateAreaSerializer(private_area, many=True)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_204_NO_CONTENT)    