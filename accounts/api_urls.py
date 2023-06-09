import rest_framework_simplejwt.views as jwt_views
from django.urls import path

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),  # verify
]
