from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name': "Python"},
    {'id':2, 'name': "JavaScript"},
    {'id':3, 'name': "Matlab"},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for r in rooms:
        if r["id"] == int(pk):
            room = r
    context = {'room': room} # room num return when go to url
    return render(request, 'base/room.html', context)