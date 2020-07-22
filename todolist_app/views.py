from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        task = Task(title = request.POST['title'])
        task.save()
        return redirect('todolist-home')
    else:
        context = {
            'tasks': Task.objects.filter(is_archived=False)
        }
        return render(request, 'todolist_app/home.html', context)

def archive(request):
    context = {
        'tasks': Task.objects.filter(is_archived=True)
    }
    return render(request, 'todolist_app/archive.html', context)