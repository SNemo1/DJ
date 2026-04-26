from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Board, Task, Comment
from .form import BoardForm, TaskForm, CommentForm

def home(request):
    if request.user.is_authenticated:
        boards = Board.objects.filter(models.Q(is_public=True) | models.Q(owner=request.user))
    else:
        boards = Board.objects.filter(is_public=True)
    return render(request, 'index.html', {'boards': boards})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            return redirect('home')
    else:
        form = BoardForm()
    return render(request, 'create_board.html', {'form': form})


def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    tasks = board.tasks.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.save()
            return redirect('board_detail', board_id=board.id)
    else:
        form = TaskForm()
    return render(request, 'board_detail.html', {'board': board, 'tasks': tasks, 'form': form})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        if 'change_status' in request.POST:
            task.status = 'Виконано' if task.status == 'В процесі' else 'В процесі'
            task.save()
            return redirect('task_detail', task_id=task.id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()

    return render(request, 'task_detail.html', {'task': task, 'comments': comments, 'form': form})