from django.urls import path, include
from rest_framework import routers
from .api import GalleryViewSet, ReadMessageView, WriteMessageView

routes = routers.DefaultRouter()
routes.register('api/gallery', GalleryViewSet, basename='gallery')
# routes.register('api/message/write', WriteMessageViewSet, basename='writeMessage')


urlpatterns = [path('', include(routes.urls)),
    path('api/message/read/<int:id>', ReadMessageView.as_view()),
    path('api/message/read', ReadMessageView.as_view()),
    path('api/message/write', WriteMessageView.as_view()),


]