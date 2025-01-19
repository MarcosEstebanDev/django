from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task
from django.http import JsonResponse


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

def tasks_list(request):
    # Example response, replace with actual data retrieval logic
    tasks = [
        {"id": 1, "name": "Task 1"},
        {"id": 2, "name": "Task 2"},
        {"id": 3, "name": "Task 3"},
    ]
    return JsonResponse(tasks, safe=False)
