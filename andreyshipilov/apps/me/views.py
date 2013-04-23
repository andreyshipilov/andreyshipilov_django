from datetime import datetime

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.db.models import Count
from django.utils.html import strip_tags
from django.utils import simplejson
import tweepy
from tweepy.error import TweepError

from me.models import ProjectType, Project, Tweet
from secret_info import *


CACHE = {
    'minute': 60,
    'hour': 60 * 60,
    'day': 60 * 60 * 24,
}


@cache_page(CACHE['day'])
def cv(request):
    return render(request, 'cv.html',)


@cache_page(CACHE['hour'] * 4)
def index(request):
    tweets, twitter_info = cache.get('tweets'), cache.get('twitter_info')

    #if not tweets:
    #    try:
    #        tweets = tweepy.api.user_timeline('andreyshipilov'),
    #        cache.set('tweets', tweets[0], CACHE['hour'])
    #    except:
    tweets = []

    if tweets and not twitter_info:
        try:
            twitter_info = tweepy.api.get_user("andreyshipilov")
            cache.set('twitter_info', twitter_info, CACHE['hour'])
        except:
            twitter_info = []

    if tweets and twitter_info:
        frequency = (datetime.today() - twitter_info.created_at).days / len(tweets)
    else:
        frequency = int()

    return render(request, 'index.html', {
        'is_index': True,
        'tweets': tweets,
        'tweet_frequency': frequency,
        'twitter_info': twitter_info,
        'projects': Project.get_published()[:30],
    })


@cache_page(CACHE['hour'] * 4)
def projects(request):
    return render(request, 'projects.html', {
        'project_types': ProjectType.objects.language().all().distinct(),
        'projects': Project.get_published(),
    })


@cache_page(CACHE['hour'] * 4)
def type_or_project(request, slug):
    objects = Project.get_published().filter(project_type__slug = slug)

    if objects.count():
        return render(request, 'projects_type.html', {
            'projects': objects,
            'type_title': ProjectType.objects.language().get(slug = slug).title
        })
    else:
        project = get_object_or_404(Project.get_published(), slug = slug)

        next = False
        try:
            next = project.get_next_by_date(is_published=True)
        except: pass

        previous = False
        try:
            previous = project.get_previous_by_date(is_published=True)
        except: pass

        return render(request, 'project.html', {
            'project': project,
            'next': next,
            'previous': previous,
            'has_screenshots': project.screenshot_set.exists(),
        })


@csrf_exempt
def everyone_tweet(request):
    if request.method == 'POST':
        text = strip_tags(request.POST.get('text', ''))
        lat = request.POST.get('lat', '')
        lng = request.POST.get('lng', '')
        country = request.POST.get('country', '')

        if 0 < len(text) <= 140:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            twitter_api = tweepy.API(auth)

            try:
                twitter_api.update_status(status=text, lat=lat, long=lng)
                tweet = Tweet(text=text, country=country, longitude=lng,
                              latitude=lat,)
                tweet.save()

                r = {
                    'status': True,
                    'text': 'Sent it like a boss.',
                }
            except TweepError, e:
                r = {
                    'status': False,
                    'text': e.reason,
                }

            return HttpResponse(simplejson.dumps(r), mimetype="text/plain")
        else:
            if len(text) == 0:
                text = 'Write at least something.'
            elif len(text) > 140:
                letter = ''
                if len(text) - 140 > 1:
                    letter = 's'
                text = 'Shorten it by %s letter%s.' % \
                       (str(len(text) - 140), letter)

            r = {
                'status': False,
                'text': text,
            }
            return HttpResponse(simplejson.dumps(r), mimetype="text/plain")
    else:
        return render(request, 'everyone_tweet.html', {
            'tweets': Tweet.objects.all(),
        })
