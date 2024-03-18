from django.urls import path
from vehicles import views

urlpatterns = [
    path(
        "api/areas/<int:area_pk>/vehicles/",
        views.RetrieveCreateVehicleView.as_view(),
    ),
    path(
        "api/areas/<int:area_pk>/vehicles/<int:vehicle_pk>/",
        views.RetrieveUpdateDeleteVehicleView.as_view(),
    ),
]
