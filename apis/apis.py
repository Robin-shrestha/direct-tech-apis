from .serializers import GallerySerializer
from .models import Gallery
from rest_framework.viewsets import ModelViewSet

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer