
from django.contrib import admin
from django.urls import path
# from app.views import Home, completed_tasks, pending_tasks, add_todo , delete_todo, mark_todo, add_todo_pending, mark_todo_pending, delete_todo_pending
from app.views import *
urlpatterns = [
    path("", Home, name = 'home'),

    path("all_tasks/", Home,name = 'home_alltasks'),
    path("all_tasks/delete_id/<int:id>", delete_todo),

    path("completed_tasks/", completed_tasks,name = "cmpt"),
    path("completed_tasks/delete_id/<int:id>", delete_todo_cmpt),
    path('completed_tasks/add-todo_cmpt/',add_todo_cmpt ),

    path("pending_tasks/", pending_tasks, name = "pt"),
    path("pending_tasks/delete_id/<int:id>", delete_todo_pending),
    path("pending_tasks/mark_complete/<int:id>/<str:status>", mark_todo_pending),
    path('pending_tasks/add-todo_pending/',add_todo_pending ),

    #todo list 
    path('add-todo/',add_todo ),
    path("delete_id/<int:id>", delete_todo),
    path("mark_complete/<int:id>/<str:status>", mark_todo)
]
