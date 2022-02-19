from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegistrationSerializer(RegisterSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        if username:
            if User.objects.filter(username=username).exists():
                msg = {'error': 'User aleady exists'}
                raise serializers.ValidationError(msg)
            else:
                return attrs
        else:
            raise serializers.ValidationError({'error': "Invalid Username"})

    def custom_signup(self, request, user):
        # general
        user.username = self.validated_data.get('username', '')

        user.save(update_fields=[
            'username',
        ])

    class Meta:
        ref_name = "CustomLoginSerializer"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get('request'),
                                    username=username, password=password)

            else:
                msg = {'error': 'Username not found'}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'error': 'Incorrect password'}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = {'error': 'Must include "deviceID" and "password".'}
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
