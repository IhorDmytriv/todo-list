from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm
from tasks.models import Task


def index(request):
    task_list = Task.objects.all().prefetch_related("tags")
    context = {
        "task_list": task_list,
    }
    return render(request, "tasks/index.html", context=context)


def toggle_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_complete = not task.is_complete
    task.save()
    return redirect("tasks:index")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
