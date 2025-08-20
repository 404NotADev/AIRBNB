from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing
from .serializers import ListingSerializer
from listings.tasks import notify_host_new_listing

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'guests', 'price'] 

    def perform_create(self, serializer):
        listing = serializer.save(owner=self.request.user)
        notify_host_new_listing.delay(listing.id)
