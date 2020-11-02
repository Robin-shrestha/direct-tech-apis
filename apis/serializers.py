from rest_framework import serializers
from .models import Gallery, Message

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class WriteMessageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Message
        fields = ['id', 'name','email', 'subject', 'message', 'date_added']

class ReadMessageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Message
        fields = ['id', 'name','email', 'subject', 'message', 'date_added', 'checked']
        read_only_fields =  ['id','name', 'email', 'subject', 'message', 'date_added']
