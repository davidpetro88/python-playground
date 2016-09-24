from django.shortcuts import render
from www.webcrowler import WebCrowlwer


def index(request):
    # webCrowler = WebCrowlwer()
    context = {
        'title': 'WebCrowler Test',
        'crowler': WebCrowlwer.getContent
    }
    return render(request, 'index.html', context)


