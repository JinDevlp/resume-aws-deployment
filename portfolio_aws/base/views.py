from django.shortcuts import render
from .models import Project
# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'home.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'project.html', context)
