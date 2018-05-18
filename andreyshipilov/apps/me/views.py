# -*- coding: utf-8 -*-

from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.utils.translation import ugettext as _
import tweepy
from tweepy.error import TweepError
from meta.views import Meta

from me.models import ProjectType, Project, Tweet
from secret_info import TWITTER_SECRETS


CACHE = {
    'minute': 60,
    'hour': 60 * 60,
    'day': 60 * 60 * 24,
}


@cache_page(CACHE['day'])
def cv(request):
    return render(request, 'cv.html', )


@cache_page(CACHE['day'])
def home(request):
    auth = tweepy.OAuthHandler(
        TWITTER_SECRETS['andreyshipilov']['consumer_key'],
        TWITTER_SECRETS['andreyshipilov']['consumer_secret'])
    auth.set_access_token(
        TWITTER_SECRETS['andreyshipilov']['access_token'],
        TWITTER_SECRETS['andreyshipilov']['access_token_secret'])
    api = tweepy.API(auth)

    try:
        tweets = api.user_timeline('andreyshipilov')
    except:
        tweets = None

    try:
        twitter_info = api.get_user('andreyshipilov')
    except:
        twitter_info = None

    if tweets and twitter_info:
        frequency = (datetime.today() - twitter_info.created_at).days / len(
            tweets)
    else:
        frequency = int()

    projects = Project.get_published()
    meta = Meta(
        url='/',
        image=projects[0].image.url,
        title=_('Andrey Shipilov'),
        description=strip_tags(_('Some text about me')),
    )

    context = {
        'is_home': True,
        'meta': meta,
        'tweets': tweets,
        'tweet_frequency': frequency,
        'twitter_info': twitter_info,
        'projects': projects[:33],
        'projects_count': projects.count()
    }

    return render(request, 'home.html', context)


@cache_page(CACHE['day'])
def projects(request):
    project_types = ProjectType.objects.language().all().distinct()
    projects = Project.get_published()
    meta = Meta(
        title=_('Projects'),
        description=_('Andrey Shipilov\'s projects'),
        keywords=[x.title for x in project_types],
        image=projects[0].image.url,
        url=request.path_info,
    )

    return render(request, 'projects.html', {
        'is_types': True,
        'meta': meta,
        'project_types': project_types,
        'projects': projects,
        'subtitle': _('Projects'),
    })


@cache_page(CACHE['day'])
def type_or_project(request, slug):
    objects = Project.get_published().filter(project_type__slug=slug)

    if objects.count():
        project_type = ProjectType.objects.language().get(slug=slug)
        title = _('Projects tagged "%s"' % project_type.title)
        meta = Meta(
            title=title,
            description=title,
            keywords=[project_type.title],
            image=objects[0].image.url,
            url=project_type.get_absolute_url(),
        )

        context = {
            'meta': meta,
            'projects': objects,
            'type_title': title + '.',
            'subtitle': title
        }
        return render(request, 'projects_type.html', context)
    else:
        project = get_object_or_404(Project.get_published(), slug=slug)
        next = False

        try:
            next = project.get_next_by_date(is_published=True)
        except:
            pass

        previous = False

        try:
            previous = project.get_previous_by_date(is_published=True)
        except:
            pass

        meta = Meta(
            title=project.title,
            description=project.explict_title + '. ' + strip_tags(project.text),
            keywords=project.project_type.language().values_list('title', flat=True),
            image=project.image.url,
            url=project.get_absolute_url(),
        )

        return render(request, 'project.html', {
            'meta': meta,
            'project': project,
            'next': next,
            'previous': previous,
            'has_screenshots': project.screenshot_set.exists(),
            'subtitle': project.title
        })


@cache_page(CACHE['hour'])
@csrf_exempt
def everyone_tweet(request):
    if request.method == 'POST':
        text = strip_tags(request.POST.get('text', ''))
        lat = request.POST.get('lat', '')
        lng = request.POST.get('lng', '')
        country = request.POST.get('country', '')

        if 0 < len(text) <= 140:
            auth = tweepy.OAuthHandler(
                TWITTER_SECRETS['everyone_tweet']['consumer_key'],
                TWITTER_SECRETS['everyone_tweet']['consumer_secret'])
            auth.set_access_token(
                TWITTER_SECRETS['everyone_tweet']['access_token'],
                TWITTER_SECRETS['everyone_tweet']['access_token_secret'])
            api = tweepy.API(auth)

            try:
                api.update_status(status=text, lat=lat, long=lng)
                tweet = Tweet(text=text, country=country, longitude=lng,
                              latitude=lat, )
                tweet.save()

                r = {
                    'status': True,
                    'text': 'Sent it like a boss.',
                }
            except TweepError, e:
                error = eval(e.reason)[0]

                r = {
                    'status': False,
                    'text': error['message'],
                }

            return JsonResponse(r)
        else:
            if len(text) == 0:
                text = 'Write at least something.'
            elif len(text) > 280:
                letter = ''
                if len(text) - 280 > 1:
                    letter = 's'
                text = 'Shorten it by %s letter%s.' % \
                       (str(len(text) - 280), letter)

            r = {
                'status': False,
                'text': text,
            }

            return JsonResponse(r)
    else:
        return render(request, 'everyone_tweet.html', {
            'tweets': Tweet.objects.all(),
        })
