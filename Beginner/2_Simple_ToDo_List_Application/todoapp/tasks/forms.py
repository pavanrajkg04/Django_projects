from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task'}))
    completed = forms.BooleanField(widget=forms.CheckboxInput(),required=False)

    class Meta:
        model = Task
        fields = "__all__" # adds all the columns to the form model