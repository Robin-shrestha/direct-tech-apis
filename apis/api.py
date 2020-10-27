from .serializers import GallerySerializer, MessageSerializer
from .models import Gallery, Message
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import authentication

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all().order_by('-date_added')
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.BaseAuthentication]

    # def get_queryset(self):
    #     return Message.objects.all().order_by('-date_added')