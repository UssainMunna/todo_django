from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from app.forms import TodoForm
from app.models import Todo
# Create your views here.

def Home(request):
    todo = TodoForm()
    fetch = Todo.objects.all()
    print(fetch)
    return render(request, 'index.html', context={ 'form' : todo, "todos" : fetch})

def pending_tasks(request):
    todo = TodoForm()
    fetch = Todo.objects.filter(status='PENDING')
    print(fetch)
    return render(request, 'pending_tasks.html',context={ 'form' : todo, "todos" : fetch})

def completed_tasks(request):
    todo = TodoForm()
    fetch = Todo.objects.filter(status= "COMPLETED")
    print(fetch)
    return render(request, 'completed_tasks.html',context={ 'form' : todo, "todos" : fetch})

def delete_todo(request, id):
    print(id)
    Todo.objects.get(pk=id).delete()
    return redirect('home')

def delete_todo_cmpt(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('cmpt')

def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        todo = form.save(commit=False)
        todo.save()
        print(todo)
        return redirect("home")
    else: 
        return render(request , 'index.html' , context={'form' : form})

def add_todo_pending(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        todo = form.save(commit=False)
        todo.save()
        print(todo)
        return redirect("pt")
    else: 
        return render(request , 'index.html' , context={'form' : form})


def mark_todo(request,id,status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def mark_todo_pending(request,id,status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('pt')

def delete_todo_pending(request, id):
    print(id)
    Todo.objects.get(pk=id).delete()
    return redirect('pt')

def add_todo_cmpt(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        todo = form.save(commit=False)
        todo.save()
        print(todo)
        return redirect("cmpt")
    else: 
        return render(request , 'index.html' , context={'form' : form})