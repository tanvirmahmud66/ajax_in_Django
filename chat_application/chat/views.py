from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import NameDB
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')

def save(request):
    name = request.POST.get('name')
    if NameDB.objects.filter(name=name).exists():
        return HttpResponse("Name already in Database")
    else:
        new_name = NameDB.objects.create(
            name=name
        )
        new_name.save()
        return HttpResponse('name save successfully')


def get_name(request):
    name = NameDB.objects.all()
    print(name)
    return JsonResponse({"name": list(name.values())})