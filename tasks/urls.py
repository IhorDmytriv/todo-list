from django.urls import path
from tasks.views import index, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
]

app_name = "tasks"
