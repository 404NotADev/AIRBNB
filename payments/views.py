from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer
from payments.tasks import send_payment_email  # импорт задачи

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        send_payment_email.delay(payment.id)
