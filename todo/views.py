from .models import Task
from django.http import HttpResponse
from django.shortcuts import redirect, render

def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task)
    return redirect('home')
# Create your views here.
