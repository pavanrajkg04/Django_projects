from django.shortcuts import render,redirect

from .models import Task
from . forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('/')

    context = {'tasks' : tasks , 'TaskForms': form}

    return render(request, 'tasks.html', context)


def updatetask(request, pk):
    
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('/')
        
    context = {'TaskForms': form}

    return render(request, 'update_task.html', context)

def deletetask(request,pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":

        task.delete()

        
        return redirect('/')
    
    context = {'task': task}

    return render(request, 'delete_task.html', context)