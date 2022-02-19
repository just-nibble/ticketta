# from django.shortcuts import render
from rest_auth.registration.views import LoginView
from .serializers import LoginSerializer
from rest_framework import permissions
# Create your views here.


class LoginView(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
