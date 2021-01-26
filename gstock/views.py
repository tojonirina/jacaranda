from django.http import HttpResponse

def index(request):
    '''
    Get index page or login page
    '''
    return HttpResponse('Hello world')
