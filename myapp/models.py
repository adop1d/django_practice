from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - "+ self.project.name +" (" + ("Completed" if self.completed else "Pending") + ")"