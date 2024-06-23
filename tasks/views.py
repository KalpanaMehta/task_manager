# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm
from django.contrib import messages

# Class-based view for listing and creating tasks
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
# Function-based view for listing tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

# Function-based view for displaying task details
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Function-based view for creating a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task-list')
        else:
            messages.error(request, 'Error adding task. Please check the form.')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Add Task', 'button_text': 'Add'})

# Function-based view for updating an existing task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
           
            return redirect('task-list')
        else:
            messages.error(request, 'Error adding task. Please check the form.')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Edit Task', 'button_text': 'Update'})

# Function-based view for deleting a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task Deleted successfully.')
          
        return redirect('task-list')
    else:
            messages.error(request, 'Error adding task. Please check the form.')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
