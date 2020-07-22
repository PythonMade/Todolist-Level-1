from django import forms
from .models import Task

# create a form that inherits from ModelForm
class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title']