from django.db import models
import string
import random
# Create your models here.

def generate_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    return code
    
def get_name():
    curr_rooms = len(Room.objects.all())
    return "Room"+curr_rooms


class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=6, default='', unique=True)
    host = models.CharField(max_length=50, unique=True, null=False)
    guest_can_skip = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


