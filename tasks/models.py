from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ['is_complete', '-created_time']

    def __str__(self):
        return f"{self.content}"
