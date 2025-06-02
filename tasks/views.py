from django.shortcuts import render

from tasks.models import Task


def index(request):
    task_list = Task.objects.all()
    context = {
        "task_list": task_list,
    }
    return render(request, "tasks/index.html", context=context)
