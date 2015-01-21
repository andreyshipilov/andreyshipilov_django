# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils.translation import ugettext as _

from meta.views import Meta

from me.models import Project
from .models import Position


def cv(request):
    title = _(u'Curriculum Vitae, Resumé')
    meta = Meta(
        title=title,
        description=_('Andrey Shipilov') + ' / ' + title,
        keywords=['CV', 'Curriculum Vitae', u'Resumé'],
    )
    context = {
        'meta': meta,
        'positions': Position.objects.all(),
        'notable_projects': Project.get_notable(),
        'subtitle': title,
    }

    return render(request, 'cv.html', context)
