from django.shortcuts import render

def home(request):
    return render(request, 'sg_home/index.html')


def about(request):
    return render(request, 'sg_home/about.html')


def not_found(request, exception):
    return render(request, 'errors/error_404.html')
