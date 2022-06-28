from rest_framework import viewsets, filters
from django.http import HttpResponse
from .serializers import UsersSerializer, MenuSerializer
from .models import Users, Menu
from rest_framework.decorators import api_view

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer

class MenuViewSet(viewsets.ModelViewSet):

    queryset = Menu.objects.all().order_by('menu_name')
    serializer_class = MenuSerializer