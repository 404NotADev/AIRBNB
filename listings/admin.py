from django.contrib import admin
from .models import Listing, ListingImage

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'city', 'price', 'max_guests')
    list_filter = ('city',)
    search_fields = ('title', 'description')

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'image')
