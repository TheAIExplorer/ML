from django.shortcuts import render, get_object_or_404
from .models import projects


def index(request):
    context = {'projects': projects.objects.all().order_by('-project_id')}

    return render(request, 'webpage/index.html', context)


def project(request, project_id):
    project_instance = get_object_or_404(projects, project_id=project_id)

    context = {'project': project_instance}
    return render(request, 'webpage/project_description.html', context)
