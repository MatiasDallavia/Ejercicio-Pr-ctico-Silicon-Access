from core.permissions import IsPrivateAreaOwner
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import PrivateAreaSerializer, UserSerializer

################### Private Area ###################


class RetrieveCreatePrivateAreaView(APIView):

    permission_classes = [IsAuthenticated]

    # Creates a single PrivateArea for specific User
    def post(self, request):

        data = request.data
        data["user"] = request.user.id

        serializer = PrivateAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieves all PrivateAreas from a specific User
    def get(self, request):
        user = request.user
        private_areas = user.privatearea_set.all()
        serializer = PrivateAreaSerializer(private_areas, many=True)
        return Response(serializer.data)


class RetrieveUpdateDeletePrivateAreaView(APIView):

    permission_classes = [IsAuthenticated, IsPrivateAreaOwner]

    # Deletes a single PrivateArea from a specific User
    def delete(self, request, area_pk):
        user = request.user

        private_area = user.privatearea_set.filter(id=area_pk, is_deleted=False).first()
        if private_area is None:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

        private_area.is_deleted = True
        private_area.save()
        return Response({"status": "successful deletion"}, status=status.HTTP_200_OK)

    # Retrieves a single PrivateArea from a specific User
    def get(self, request, area_pk):
        user = request.user

        private_area = user.privatearea_set.filter(id=area_pk, is_deleted=False).first()
        if private_area is None:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PrivateAreaSerializer(private_area)
        return Response(serializer.data)

    # Updates a single PrivateArea from a specific User
    def put(self, request, area_pk):

        user = request.user
        request.data["user"] = user.id

        private_area = user.privatearea_set.filter(id=area_pk, is_deleted=False).first()
        if private_area is None:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PrivateAreaSerializer(private_area, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################### User ###################


class UserRegistration(APIView):

    # Creates User
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveToken(APIView):
    authentication_classes = [TokenAuthentication]

    # Create a Token for User authentication
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

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
