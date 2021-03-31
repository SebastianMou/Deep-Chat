from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2012'
    },
    {
        'author': 'sebas',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'april 17, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')