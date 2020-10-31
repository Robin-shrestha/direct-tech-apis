from django.urls import path, include
from rest_framework import routers
from .api import GalleryViewSet, WriteMessageViewSet, ReadMessageView

routes = routers.DefaultRouter()
routes.register('api/gallery', GalleryViewSet, basename='gallery')
routes.register('api/messages/write', WriteMessageViewSet, basename='writeMessage')


urlpatterns = [path('', include(routes.urls)),
    path('api/message/read/<int:id>', ReadMessageView.as_view()),
    path('api/message/read', ReadMessageView.as_view()),

]