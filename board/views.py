from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def board(request, room_name):
    return render(request, 'board/chat.html', {'room_name_json':mark_safe(json.dumps(room_name))})