from django.shortcuts import render
from .models import Task

def home(request):
    context = {
        'tasks': Task.objects.filter(is_archived=False)
    }
    return render(request, 'todolist_app/home.html', context)

def archive(request):
    context = {
        'tasks': Task.objects.filter(is_archived=True)
    }
    return render(request, 'todolist_app/archive.html', context)