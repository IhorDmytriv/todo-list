from django.urls import path
from tasks.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_status,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

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
    path(
        "tasks/<int:pk>/toggle-task-status/",
        toggle_task_status,
        name="toggle-task-status"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/update/<int:pk>/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/delete/<int:pk>/",
        TagDeleteView.as_view(),
        name="tag-delete"
    )
]

app_name = "tasks"
