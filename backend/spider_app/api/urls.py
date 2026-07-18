from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, TagViewSet, SpiderViewSet, SpiderImgViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"tags", TagViewSet)
router.register(r"spiders", SpiderViewSet)
router.register(r"spidersImg", SpiderImgViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
