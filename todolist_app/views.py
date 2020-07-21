from django.shortcuts import render

def home(request):
    return render(request, 'todolist_app/home.html')

def archive(request):
    return render(request, 'todolist_app/archive.html')