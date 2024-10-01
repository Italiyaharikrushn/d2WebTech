from django.shortcuts import render, redirect
from .models import Todo
import datetime

# Display the list of todos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# Create a new todo
def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Todo.objects.create(name=name)
            # messagebox.showinfo("Insert", "Inserted Successfully")
        return redirect('todo_list')

# Delete a specific todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
    

# Update a specific todo
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
