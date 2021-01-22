# from django.db.models import fields
from rest_framework import serializers
from .models import Room

# """
#     Class Meta - to add meta data to our model
# """

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at') # these fields we craeted in our models.py    

# to validate the data
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')