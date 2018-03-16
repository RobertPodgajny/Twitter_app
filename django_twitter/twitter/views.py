from django.shortcuts import render
from django.views import View
from twitter.models import Tweet


class MainPageView(View):
    def get(self, request):
        return render(request,
                      template_name='base.html')


class AllTweetsView(View):
    def get(self, request):
        tweets = Tweet.objects.all().order_by("creation_date")
        ctx = {
            'tweets': tweets,
        }
        return render(request,
                      template_name='all_tweets.html',
                      context=ctx)

