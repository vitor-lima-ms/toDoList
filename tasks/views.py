from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

import requests

from tasks.models import Tasks
from tasks.myForms import TaskSearchNotCompleted, TaskSearchCompleted, CreateTask

# Create your views here.

def TaskCreateView(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:taskList')
    else:
        form = CreateTask()
    return render(request, 'taskCreate.html', {'form': form})

def TaskListView(request):
    notCompletedTasks = Tasks.objects.filter(completed=False)
    taskSearch = TaskSearchNotCompleted()
    context = {
        'tasks': notCompletedTasks,
        'taskSearch': taskSearch,
    }
    return render(request, 'taskList.html', context)

def searchTaskNotCompleted(request):
    if request.method == 'POST':
        taskSearch = TaskSearchNotCompleted(request.POST)
        if taskSearch.is_valid():
            task = taskSearch.cleaned_data['task']
            return render(request, 'taskSearchNotCompleted.html', {'task': task})

def completeTask(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.completed = True
    task.save()
    return redirect('tasks:completedTasks')

def workTasks(request):
    tasks = Tasks.objects.filter(category='work', completed=False)
    return render(request, 'taskList.html', {'tasks': tasks})

def studiesTasks(request):
    tasks = Tasks.objects.filter(category='studies', completed=False)
    return render(request, 'taskList.html', {'tasks': tasks})

def personalTasks(request):
    tasks = Tasks.objects.filter(category='personal', completed=False)
    return render(request, 'taskList.html', {'tasks': tasks})

def shoppingTasks(request):
    tasks = Tasks.objects.filter(category='shopping', completed=False)
    return render(request, 'taskList.html', {'tasks': tasks})

def otherTasks(request):
    tasks = Tasks.objects.filter(category='other', completed=False)
    return render(request, 'taskList.html', {'tasks': tasks})

def deleteTaskList(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks:taskList')

def completedTasks(request):
    tasks = Tasks.objects.filter(completed=True)
    taskSearch = TaskSearchCompleted()
    context = {
        'tasks': tasks,
        'taskSearch': taskSearch,
    }
    return render(request, 'completedTasks.html', context)

def deleteTaskCompleted(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks:completedTasks')

def searchTaskCompleted(request):
    if request.method == 'POST':
        taskSearch = TaskSearchCompleted(request.POST)
        if taskSearch.is_valid():
            task = taskSearch.cleaned_data['task']
            return render(request, 'taskSearchCompleted.html', {'task': task})