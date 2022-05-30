from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class TheatrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theatr
        fields = '__all__'


class SoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soon
        fields = '__all__'


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class SeansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seans
        fields = '__all__'


class TSeansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TSeans
        fields = '__all__'