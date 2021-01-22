from django.db import models
import string
import random
from datetime import datetime

# Create your models here.

def unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

class Room(models.Model):
    # each room will have a code to enter with and a host
    # a permission to pause by guest

    code = models.CharField(max_length=8, unique=True, default=unique_code)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(default=datetime.now()) #, auto_now_add=True