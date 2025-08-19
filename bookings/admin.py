from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'guest', 'check_in', 'check_out', 'price')
    list_filter = ('check_in', 'check_out')
    search_fields = ('listing__title', 'guest__username')
