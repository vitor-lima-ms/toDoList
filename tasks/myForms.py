from django import forms

from tasks.models import Tasks

class TaskSearchNotCompleted(forms.Form):
    task = forms.ModelChoiceField(
        queryset=Tasks.objects.filter(completed=False),
        label="Select a task to search for"
    )

class TaskSearchCompleted(forms.Form):
    task = forms.ModelChoiceField(
        queryset=Tasks.objects.filter(completed=True),
        label="Select a completed task to search for"
    )