from django.shortcuts import render
from www.webcrowler import WebCrowlwer


def index(request):
    web_crowler = WebCrowlwer()
    context = {
        'title': 'WebCrowler Test',
        'webCrowler': web_crowler.get_content()
    }
    return render(request, 'index.html', context)