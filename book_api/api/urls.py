from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
] + router.urls


urlpatterns += [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]