from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Directories

# Create your views here.

def home(request):
    '''
    Get all directories 
    '''
    try:
        directories = Directories.objects.all()
    except:
        return HttpResponse('Not found', status=500)

    return render(request, 'directory_index.html', {'directories':directories})

def store(request):
    '''
    Store a directory
    '''
    try:
        if request.method == 'POST':

            newDirectory = Directories()
            newDirectory.full_name = request.POST['full_name']
            newDirectory.gender = request.POST['gender']
            newDirectory.function = request.POST['function']
            newDirectory.phone = request.POST['phone']
            newDirectory.urgent_phone = request.POST['urgent_phone']
            newDirectory.email = request.POST['email']
            newDirectory.address = request.POST['address']
            newDirectory.date_of_service = request.POST['date_of_service']
            newDirectory.end_of_service = request.POST['end_of_service']
            newDirectory.state = request.POST['state']
            newDirectory.notes = request.POST['notes']
            newDirectory.avatar = 'myavatar'

            newDirectory.save()

        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        return HttpResponse('Error', status=500)

    return redirect('directories:directory_home')

def show(request, id):
    '''
    Show all information of a specific directory
    '''
    try:
        directory = Directories.objects.get(id=int(id))
    except:
        raise Http404('Not found')

    return render(request, 'show_directory.html', {'directory':directory}) 

def edit(request, id):
    '''
    Edit information about a specific directory
    '''
    try:
        directory = Directories.objects.get(id=int(id))
    except:
        raise Http404('Not found')

    return render(request, 'edit_directory.html', {'directory':directory})

def update(request, id):
    '''
    Update a specific directory
    '''
    try:
        if request.method == 'POST':

            directory = Directories.objects.get(id=int(id))
            directory.full_name = request.POST['full_name']
            directory.function = request.POST['function']
            directory.gender = request.POST['gender']
            directory.phone = request.POST['phone']
            directory.urgent_phone = request.POST['urgent_phone']
            directory.email = request.POST['email']
            directory.address = request.POST['address']
            directory.date_of_service = request.POST['date_of_service']
            directory.end_of_service = request.POST['end_of_service']
            directory.state = request.POST['state']
            directory.avatar = request.POST['avatar']
            directory.notes = request.POST['notes']

            directory.save()

        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        return HttpResponse('Error', status=500)

    return redirect('directories:show_directory', id)

def delete(request, id):
    """
    Delete a specific directory
    """
    try:
        if request.method == 'POST':
            directory = Directories.objects.get(id=int(id))
            directory.delete()
        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        raise Http404('Not found')

    return redirect('directories:directory_home')