from django.http.response import Http404
from django.shortcuts import render

# Create your views here.


def home(request):
    try:
        print('Hello')
    except:
        raise Http404('Page not found')

    return render(request, 'computer_index.html')

def store(request):
    pass

def show(request, id):
    pass

def edit(request, id):
    pass

def update(request, id):
    pass