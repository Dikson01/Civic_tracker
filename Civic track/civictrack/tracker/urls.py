from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CivicIssueViewSet

router = DefaultRouter()
router.register(r'tracker', CivicIssueViewSet, basename='tracker')

urlpatterns = [
    path('', include(router.urls)),
]

