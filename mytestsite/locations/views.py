from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the locations index.")


def index_with_arg(request, add_something):
    return render(request, 'test.html', {'press': add_something})