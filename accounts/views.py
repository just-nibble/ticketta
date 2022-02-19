from django.shortcuts import render
from rest_auth.registration.views import RegisterView, LoginView
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework import permissions
# Create your views here.


class Login(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print("Haba")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Serializer: ", serializer)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
