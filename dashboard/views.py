from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    context = {
        "page_title": 'Home'
    }
    return render(request, 'home.html', context)
