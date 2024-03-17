from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission
from users.models import PrivateArea


class IsPrivateAreaOwner(BasePermission):

    def has_permission(self, request, view):
        area_pk = request.parser_context["kwargs"]["area_pk"]
        user = request.user
        private_area = PrivateArea.objects.filter(id=area_pk, is_deleted=False).first()

        if private_area is None:
            raise NotFound("Private area does not exists")

        return private_area.user == user
