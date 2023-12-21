from django.shortcuts import render
from django.http import HttpResponse
from .models import Room, Topic, Message



def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room} # room num return when go to url
    return render(request, 'base/room.html', context)

def create_room(request):
    context = {}
    return render(request, 'base/room_form.html', context)