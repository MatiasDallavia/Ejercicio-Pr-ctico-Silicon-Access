from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission


class IsPrivateAreaOwner(BasePermission):

    def has_permission(self, request, view):
        id = request.parser_context["kwargs"]["area_pk"]
        user = request.user
        private_area = user.privatearea_set.filter(id=id).first()
        print(private_area)

        if private_area:
            return True
        raise NotFound(f"Private area not found")
