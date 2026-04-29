from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-board/', views.create_board, name='create_board'),
    path('board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]