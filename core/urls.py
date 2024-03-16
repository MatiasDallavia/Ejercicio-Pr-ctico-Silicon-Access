from django.contrib import admin
from django.urls import path

from users import views
from vehicles import views as vi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", views.UserRegistration.as_view()),
    path("users/auth-token/", views.RetrieveToken.as_view()),
    path("areas/", views.RetrieveCreatePrivateAreaView.as_view()),
    path(
        "areas/<int:area_pk>/",
        views.RetrieveUpdateDeletePrivateAreaView.as_view(),
        name="area-single",
    ),
    path(
        "areas/<int:area_pk>/vehicles/",
        vi.RetrieveCreateVehicleView.as_view(),
        name="area-single",
    ),
    path(
        "areas/<int:area_pk>/vehicles/<int:vehicle_pk>/",
        vi.RetrieveUpdateDeleteVehicleView.as_view(),
        name="area-single",
    ),
]
