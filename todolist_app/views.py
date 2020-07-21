from django.shortcuts import render

tasks = [
    {
        'title': 'Task 1',
        'is_achived': False,
        'date_created': 'July 1, 2020',
    },
    {
        'title': 'Task 2',
        'is_achived': False,
        'date_created': 'July 1, 2020',
    },
    {
        'title': 'Task 3',
        'is_achived': False,
        'date_created': 'July 1, 2020',
    },
    {
        'title': 'Task 4',
        'is_achived': False,
        'date_created': 'July 1, 2020',
    },
    {
        'title': 'Task 5',
        'is_achived': False,
        'date_created': 'July 1, 2020',
    },
]

def home(request):
    context = {
        'tasks': tasks,
    }
    return render(request, 'todolist_app/home.html', context)

def archive(request):
    return render(request, 'todolist_app/archive.html')