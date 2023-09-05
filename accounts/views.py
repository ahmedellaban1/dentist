from django.shortcuts import render, redirect

def dr_nagib_cv(request):
    return render(request, 'dr_nagib.html', context=None)