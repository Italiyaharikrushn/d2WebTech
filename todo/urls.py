from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name="todo_list"),
    path('todo/create/', views.create_todo, name="create_todo"),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name="delete_todo"),
    path('todo/update/<int:todo_id>/', views.update_todo, name='update_todo'),
    # path('todo/complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
]