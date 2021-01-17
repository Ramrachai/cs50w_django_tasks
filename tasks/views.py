from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.
tasks = ['hello', 'mello', 'yello']

class TaskFormObj(forms.Form): 
    Ram_task_form = forms.CharField(label="New Task")


def index(req):
    return render(req, 'index.html', {
        "tasks": tasks 
    })

def add(req):

    if req.method == "POST":
        form = TaskFormObj(req.POST)
        if form.is_valid():
            task = form.cleaned_data["Ram_task_form"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(req, "add.html", {
                "form": form
            })


    return render(req, 'add.html' , {
        'form': TaskFormObj()
    })
