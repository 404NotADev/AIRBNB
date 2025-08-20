from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'guest', 'check_in', 'check_out', 'price']

    def validate(self, data):
        listing = data.get("listing")
        check_in = data.get("check_in")
        check_out = data.get("check_out")

        if check_in >= check_out:
            raise serializers.ValidationError("Дата выезда должна быть позже даты заезда.")

        
        overlapping = Booking.objects.filter(
            listing=listing,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status="confirmed"  
        ).exists()

        if overlapping:
            raise serializers.ValidationError("Эти даты уже забронированы.")

        return data
