import math
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import User, Tweet
from django.core.paginator import Paginator

ITEMS_PER_PAGE = 50


def _get(request, param, default=None):
    value = request.GET.get(param)
    if value is None:
        if default is None:
            raise Http404()
        else:
            return default
    return value


def _search(query, *items):
    tokens = query.split(" ")
    unused_tokens = [token for token in tokens]
    for token in tokens:
        for item in items:
            if token.lower() in item.lower():
                if token in unused_tokens:
                    unused_tokens.remove(token)
    return len(unused_tokens) == 0


def index(request):
    context = {}
    return render(request, "tracker/index.html", context)


def figures(request):
    figures = User.objects.all()
    search = _get(request, "search", default="")
    matched_figures = []
    page = int(_get(request, "page", default=1))
    if len(search) > 0:
        for figure in figures:
            if _search(search, figure.full_data["name"], figure.full_data["screen_name"], figure.full_data["description"]):
                matched_figures.append(figure)
    else:
        matched_figures = figures
    url_parameters = "&search=%s" % search
    paginator = Paginator(matched_figures, 30)
    page_obj = paginator.get_page(page)
    context = {
        "all_figures": User.objects.count(),
        "total_matched": len(matched_figures),
        "figures": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "search_query": search,
        "url_parameters": url_parameters
    }
    return render(request, "tracker/figures.html", context)


def figure(request):
    user_id = _get(request, "account")
    user = get_object_or_404(User, user_id=user_id)
    context = {
        "figure": user,
        "active": "overview",
        "tweets": Tweet.objects.filter(user=user, deleted=True).order_by("-modified_date")[:4],
        "total_archived": Tweet.objects.filter(user=user).count()
    }
    return render(request, 'tracker/figure.html', context)


def tweets(request):
    user_id = _get(request, "account")
    user = get_object_or_404(User, user_id=user_id)
    deleted = _get(request, "deleted", default="False") == "True"
    search = _get(request, "search", default="")
    page = int(_get(request, "page", default=1))
    active = "deleted" if deleted else "archive"
    tweets = Tweet.objects.filter(user=user, deleted=deleted).order_by("-modified_date")
    paginator = Paginator(tweets, 30)
    page_obj = paginator.get_page(page)
    context = {
        "figure": user,
        "active": active,
        "search": search,
        "page_obj": page_obj,
        "tweets": page_obj,
        "paginator": paginator,
        "url_parameters": "&deleted=%s&account=%s&search=%s" % (deleted, user_id, search)
    }
    return render(request, 'tracker/tweets.html', context)


def tweet(request):
    tweet_id = _get(request, "tweet")
    return HttpResponse("You are looking at the tweet page.")
