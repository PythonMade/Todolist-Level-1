from django.shortcuts import render, redirect
from django.contrib import messages
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

def deleteTask(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    task.delete()
    return redirect('todolist-home')

def archiveTask(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    task.is_archived = True
    task.save()
    messages.success(request, f'A task has been archived')
    return redirect('todolist-home')

def unArchiveTask(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    task.is_archived = False
    task.save()
    messages.success(request, f'A task has been un-archived')
    return redirect('todolist-archive')