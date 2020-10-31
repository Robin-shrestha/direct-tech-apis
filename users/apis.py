from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginSerializer, UserSerializer
from rest_framework import permissions, generics
from rest_framework import status

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    # def post(self, request, *args,**kwargs):
    #     seralizer = self.get_serializer(data = request.data)
    #     seralizer.isvalid(raise_exception = True)
    #     user = seralizer.validated_data
    #     _, token = AuthToken.objects.create(user)
    #     return Response( {
    #         'token':token
    #     }, status=status.HTTP_202_ACCEPTED)

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            _, token = AuthToken.objects.create(user)
            return Response({
                'user':UserSerializer(user, context=self.get_serializer_context()).data,
                'token':token
            }, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'message':'invalid credentials', 
            'errors':serializer.errors
            }, status=status.HTTP_403_FORBIDDEN)

    
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    
