from django.shortcuts import render
from .models import projects


def index(request):
    context = {'projects': projects.objects.all()}

    return render(request, 'webpage/index.html', context)
