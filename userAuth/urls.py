from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
        path('login/',views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
        path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
        path('register/',views.UserRegistrationView.as_view(),name='register')
    ]
    