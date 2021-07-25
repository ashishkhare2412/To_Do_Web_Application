from django import forms
from .models import TodolistModel

class TodolistForm(forms.ModelForm):
    class Meta:
        model = TodolistModel
        fields = ['task'] 

        widgets = {'task':forms.Textarea(attrs={'rows':5,'cols':22,'style':'resize:none','placeholder':'write task here'})}