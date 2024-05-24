from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home page")

def about(request):
    return HttpResponse("Welcome to the about page")