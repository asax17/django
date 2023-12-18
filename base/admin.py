from django.contrib import admin
from .models import Room, Topic, Message

admin.site.register(Room) # accessible through admin
admin.site.register(Topic) 
admin.site.register(Message) 