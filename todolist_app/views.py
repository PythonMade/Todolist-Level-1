from django.shortcuts import render

def home(request):
    return render(request, 'todolist_app/home.html')
