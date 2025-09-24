from django.urls import path
from . import views  # Import the view functions

urlpatterns = [
    path('',views.index, name='index'),  # Added this line to map the root URL to the hello_world view,
    path('about/', views.about, name='about'),
    path('hello/<str:username>',views.hello_world, name='hello'),
    path('projects/', views.projects, name ='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
]