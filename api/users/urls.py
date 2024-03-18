from django.urls import path

from users import views

urlpatterns = [
    path("api/users/", views.UserRegistration.as_view()),
    path("api/users/auth-token/", views.RetrieveToken.as_view()),
    path("api/areas/", views.RetrieveCreatePrivateAreaView.as_view()),
    path(
        "api/areas/<int:area_pk>/",
        views.RetrieveUpdateDeletePrivateAreaView.as_view(),
    ),
]
