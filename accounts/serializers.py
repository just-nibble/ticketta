from rest_framework import serializers, exceptions
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegistrationSerializer(RegisterSerializer):

    username = None
    deviceID = serializers.CharField()

    def validate(self, attrs):
        deviceID = attrs.get('deviceID')
        if deviceID:
            if User.objects.filter(deviceID=deviceID).exists():
                msg = {'error': 'User aleady exists'}
                raise serializers.ValidationError(msg)
            else:
                return attrs
        else:
            raise serializers.ValidationError({'error': "No device id"})

    def custom_signup(self, request, user):
        # general
        user.deviceID = self.validated_data.get('deviceID', '')

        user.save(update_fields=[
            'deviceID',
        ])

    class Meta:
        ref_name = "CustomLoginSerializer"
        read_only_fields = ("deviceId", )


class LoginSerializer(serializers.Serializer):
    deviceID = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        deviceID = attrs.get('deviceID')
        password = attrs.get('password')

        if deviceID and password:
            if User.objects.filter(deviceID=deviceID).exists():
                user = authenticate(request=self.context.get('request'),
                                    deviceID=deviceID, password=password)

            else:
                msg = {'error': 'Device is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'error': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = {'error': 'Must include "deviceID" and "password".'}
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
