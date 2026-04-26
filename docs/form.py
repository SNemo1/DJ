from django import forms
from .models import Board, Task, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'is_public']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']