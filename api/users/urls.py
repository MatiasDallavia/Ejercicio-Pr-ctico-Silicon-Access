from django.urls import path

from users import views

urlpatterns = [
    path("users/", views.UserRegistration.as_view()),
    path("users/auth-token/", views.RetrieveToken.as_view()),
    path("areas/", views.RetrieveCreatePrivateAreaView.as_view()),
    path(
        "areas/<int:area_pk>/",
        views.RetrieveUpdateDeletePrivateAreaView.as_view(),
    ),
]
