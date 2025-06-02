from django import forms
from .models import Task
from django.forms.widgets import DateInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_complete', 'tags']
        widgets = {
            'deadline': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }
