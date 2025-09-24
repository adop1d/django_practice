from django.http import HttpResponse
from .models import Task,Project
from .forms import createNewTaskForm, createNewProjectForm
from django.shortcuts import render,redirect

# Create your views here.
def index (request):
    title = "Welcome to my app!!"
    return render(request, 'index.html', {'title': title})

def about(request):
    username = "Kelvin"
    return render(request, 'about.html', {'username': username })

def hello_world(request, username):
    print(username)
    return HttpResponse("<h1>Hello, %s <h1>" % username)


def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    #task = get_object_or_404(Task)
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'task': task})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': createNewTaskForm(), 'success': True})

    else:
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': createNewProjectForm()})
    else:
        Project.objects.create(
            name = request.POST['name'])
        redirect('projects')