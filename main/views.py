from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def home(request):
    return render(request, 'home.html', {})