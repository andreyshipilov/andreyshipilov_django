from django.shortcuts import render

from me.models import Project
from .models import Position


def cv(request):
    context = {
        'positions': Position.objects.all(),
        'notable_projects': Project.get_notable(),
    }

    return render(request, 'cv.html', context)
