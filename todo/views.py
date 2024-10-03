from django.shortcuts import render, redirect
from .models import Todo
import datetime

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Todo.objects.create(name=name)
        return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
    
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            todo.name = name
            todo.save()
        return redirect('todo_list')
    return render(request, 'todo/index.html', {'todo': todo})
        
def complate_todo(request, todo_id):
    todo_id = Todo.objects.get(id = todo_id)
    if request.method == 'GET':
        time_date = datetime.now()
        time_date.save()
        return redirect('todo_list')
    else:
        return False

