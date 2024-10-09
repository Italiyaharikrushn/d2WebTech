from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Todo list function
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# Create function
def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        is_complete = 'complete' in request.POST
        date = request.POST.get('date') if is_complete else None
        
        if name:
            Todo.objects.create(name=name, description=description, date=date, is_complete=is_complete)

        return redirect('todo_list')

# Delete function
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

# Update function  
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        is_complete = 'completed' in request.POST
        date = request.POST.get('dated') if is_complete else None

        # Update fields if provided
        if name:
            todo.name = name
            todo.description = description
            todo.date = date
            todo.is_complete = is_complete
            todo.save()
        return redirect('todo_list')

    return render(request, 'todo/index.html', {'todo': todo})

# Complete function
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
#         if 'complete' in request.POST:
#             todo.is_complete = True
#         elif 'incomplete' in request.POST:
#             todo.is_complete = False
#         todo.save()
        todo.is_complete = 'complete' in request.POST
        todo.save()
        return redirect('todo_list')
    
    return render(request, 'todo/index.html', {'todo': todo})
