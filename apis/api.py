from .serializers import GallerySerializer, ReadMessageSerializer, WriteMessageSerializer
from .models import Gallery, Message
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]


class WriteMessageViewSet(ModelViewSet):
    queryset = Message.objects.all().order_by('-date_added')
    serializer_class = WriteMessageSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.BaseAuthentication]

    # def get_queryset(self):
    #     return Message.objects.all().order_by('-date_added')

class ReadMessageView(views.APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def get_object(self,id):
        try:
            return Message.objects.get(pk=id)
        except:
            return Response(f'no messsage of id={id}', status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, id=None):
        if(id==None):
            item = Message.objects.all().order_by('-date_added')
            many=True
        else:
            item = self.get_object(id)
            many=False
        serializer = ReadMessageSerializer(item, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = request.data
        message = self.get_object(id)
        message.checked = data['checked']
        message.save()
        serializer = ReadMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        message = self.get_object(id)
        message.delete()
        return Response(status=status.HTTP_200_OK)



    