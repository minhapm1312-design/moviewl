from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.movie_create, name='movie_create'),
    path('edit/<int:id>/', views.movie_update, name='movie_update'),
    path('delete/<int:id>/', views.movie_delete, name='movie_delete'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]