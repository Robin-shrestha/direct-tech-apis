from django.urls import path, include
from rest_framework import routers
from .apis import GalleryViewSet

routes = routers.DefaultRouter()
routes.register('api/gallery', GalleryViewSet, basename='gallery')

urlpatterns = [path('', include(routes.urls)),]