from django.http import HttpResponse
from .models import Task,Project
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello_world(request, username):
    print(username)
    return HttpResponse("<h1>Hello, %s <h1>" % username)


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    #task = get_object_or_404(Task)
    return render(request, 'tasks.html')