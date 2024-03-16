from django.contrib import admin
from django.urls import path
from users import views
from vehicles import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserRegistration.as_view()),
    path('users/auth-token/', views.GetToken.as_view()),
    path('areas/', views.ListPrivateAreaView.as_view()),
    path('areas/<int:area_pk>/', views.SinglePrivateAreaView.as_view(), name="area-single"),
    path('areas/<int:area_pk>/vehicles/', vi.ListVehicleView.as_view(), name="area-single"),
    path('areas/<int:area_pk>/vehicles/<int:vehicle_pk>/', vi.SingleVehicleView.as_view(), name="area-single"),
]
