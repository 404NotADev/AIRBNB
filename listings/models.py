from django.db import models
from django.conf import settings  # для ForeignKey на User

class Listing(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    max_guests = models.IntegerField()

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_images/')

    def __str__(self):
        return f"{self.listing.title} image"
