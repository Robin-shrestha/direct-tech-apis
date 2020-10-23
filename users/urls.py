from django.urls import path, include
from .apis import LoginApi, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth/login', LoginApi.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/user', UserAPI.as_view(), ),

]