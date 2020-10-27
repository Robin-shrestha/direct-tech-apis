from django.urls import path, include
from rest_framework import routers
from .api import GalleryViewSet, MessageViewSet

routes = routers.DefaultRouter()
routes.register('api/gallery', GalleryViewSet, basename='gallery')
routes.register('api/messages', MessageViewSet, basename='messages')


urlpatterns = [path('', include(routes.urls)),]