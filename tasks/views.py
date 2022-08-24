from turtle import title
from django.shortcuts import render, redirect
from .models import Tasks
# Create your views here.
def list_tasks(request):
    tasks = Tasks.objects.all()
    print (tasks)
    return render (request, 'list_tasks.html', {'tasks' : tasks})

def create_task(request):
    task = Tasks(
        title=request.POST['title'], 
        description=request.POST['description']
    )
    task.save()
    print(request.POST)
    return redirect('/')

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('/')