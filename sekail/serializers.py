from rest_framework import serializers

from rest_framework_jwt.settings import api_settings
from .models import (
    User,
    Device,
    Store,
    Customer
    )


def assign_token(user_instance):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user_instance)
    token = jwt_encode_handler(payload)
    return token


class CreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'password', 'email', 'token']

class UserCreateSerializer(CreateSerializer):
    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        token = assign_token(new_user)
        validated_data["token"] = token
        return validated_data


class StoreCreateSerializer(CreateSerializer):
    def create(self, validated_data):
        validated_data['is_store']=True
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        token = assign_token(new_user)
        validated_data["token"] = token
        return validated_data



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name', 
            'email',           
        ]