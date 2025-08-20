from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, CreatePaymentIntentView, stripe_webhook

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')  

urlpatterns = [
    path('', include(router.urls)),
    path('create-intent/', CreatePaymentIntentView.as_view(), name='create-intent'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]
