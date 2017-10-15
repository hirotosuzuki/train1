from django.shortcuts import render
from gunosynews.models import Gunosy
# Create your views here.

def index(request):
    article_title = Gunosy.objects.all()
    context = {
        'article_title': article_title
    }
    return render(request, 'gunosynews/index.html', context)
