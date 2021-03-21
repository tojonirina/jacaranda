from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    '''
    Get index page or login page
    '''
    return HttpResponse('Hello world')

def pageNotFound(request, exception=None):
    return render( request, 'errors/404.html')

def unauthorizedRequest(request, exception=None):
    return HttpResponse('Error 403', status=403)

def serverError(request, exception=None):
    return HttpResponse('Error 500', status=500)