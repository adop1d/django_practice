from django import forms


class createNewTaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(label= "descripcion de la tarea",widget=forms.Textarea)


class createNewProjectForm(forms.Form):
    name = forms.CharField(label="Project Name", max_length=100)