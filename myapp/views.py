from django.http import HttpResponse
from .models import Task,Project
from django.shortcuts import get_object_or_404, render

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
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    #task = get_object_or_404(Task)
    return render(request, 'tasks.html')