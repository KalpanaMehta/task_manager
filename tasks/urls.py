from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy,task_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    # API endpoints
    path('api/tasks/', TaskListCreate.as_view(), name="task-list-create"),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
  
    # Front-end views
    path('tasks', task_list, name='task-list'),
    path('tasks/new/', task_create, name='task-create'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),  # task id part
    path('tasks/<int:pk>/edit/', task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
]
