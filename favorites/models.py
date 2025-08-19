from django.db import models
from listings.models import Listing
from users.models import User

class Favorite(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'user')
