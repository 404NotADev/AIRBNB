from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet  

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
