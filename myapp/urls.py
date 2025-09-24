from django.urls import path
from . import views  # Import the view functions

urlpatterns = [
    path('',views.index),  # Added this line to map the root URL to the hello_world view,
    path('home/about/', views.about),
    path('<str:username>',views.hello_world),
    path('home/projects/', views.projects),
    path('home/tasks/', views.tasks),
    path('home/create_task/', views.create_task),
    path('home/create_project/', views.create_project),
]