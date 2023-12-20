from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        managed = True
        verbose_name = 'UserSerializer'
        verbose_name_plural = 'UserSerializers'
        fields = ['username', 'password']
