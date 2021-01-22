
from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.serializers import Serializer
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
from datetime import datetime

# Create your views here.

"""
To create or view a room - call the Room class and the serializer
"""


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format= None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            # created_at = serializer.data.get('created_at')
            host = self.request.session.session_key
            # Search if a user has an existing room based on host info
            queryset = Room.objects.filter(host=host)
            # print('Queryset = ', queryset)
            # if it exists, then updatethe new info
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.created_at = datetime.now()
                room.save(update_fields=['guest_can_pause', 'votes_to_skip', 'created_at'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()

                # we return some response (the room info) -> RoomSerializer(room), 
                # which we need serialize in json format -> (.data)
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)