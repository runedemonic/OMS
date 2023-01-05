from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import urls

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('api-jwt-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-jwt-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-jwt-auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
