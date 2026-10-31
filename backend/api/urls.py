from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("services", ServiceViewSet)
router.register("projects", ProjectViewSet)
router.register("gallery", GalleryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("company/", CompanyView.as_view()),
    path("enquiries/", EnquiryCreateView.as_view()),
    path("contact/", ContactCreateView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
