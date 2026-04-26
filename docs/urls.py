from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('register/', views.register, name='register'),
]