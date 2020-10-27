from rest_framework import serializers
from .models import Gallery, Message

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Message
        fields = '__all__'