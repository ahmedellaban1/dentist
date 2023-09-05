from django.shortcuts import render, redirect


def dr_nagib_cv(request):
    return render(request, 'dr_nagib.html', context=None)


def about_developer(request):
    return render(request, 'about_developer.html', context=None)
