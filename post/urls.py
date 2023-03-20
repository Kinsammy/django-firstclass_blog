from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('post_detail/<int:pk>/', views.post_detail, name='detail'),
    path('greet/', views.greet, name='greet'),
    path('salut/', views.salut, name='salut'),
]
