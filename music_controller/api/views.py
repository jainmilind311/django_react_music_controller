from django.shortcuts import render
from django.http import HttpResponse
from .serializers import RoomSerializers
from rest_framework import generics
from .models import Room
# Create your views here.


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializers