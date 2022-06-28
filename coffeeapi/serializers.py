from rest_framework import serializers
from .models import Users, Menu

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'birth_date', 'gender', 'email', 'password')

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name', 'price', 'image', 'temperature')