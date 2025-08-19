from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer
from bookings.tasks import send_booking_email  

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        booking = serializer.save(guest=self.request.user)
        send_booking_email.delay(booking.id)

