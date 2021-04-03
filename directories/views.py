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

    return render(request, 'directory/home.html', {'directories':directories})

def store(request):
    '''
    Store a directory
    '''
    try:
        if request.method == 'POST':

            directory = Directories()
            directory.full_name = request.POST['full_name'].upper()
            directory.gender = request.POST['gender']
            directory.date_of_birth = request.POST['date_of_birth']
            directory.place_of_birth = request.POST['place_of_birth']
            directory.cin = request.POST['cin']
            directory.delivered_on = request.POST['delivered_on']
            directory.delivered_at = request.POST['delivered_at']
            directory.phone = request.POST['phone']
            directory.urgent_phone = request.POST['urgent_phone']
            directory.email = request.POST['email']
            directory.address = request.POST['address']
            directory.function = request.POST['function']
            directory.departement = request.POST['departement']
            directory.date_of_service = request.POST['date_of_service']
            directory.end_of_service = request.POST['end_of_service']
            directory.matricule_number = request.POST['matricule_number']
            directory.state = 1
            directory.avatar = 'myavatar'
            directory.notes = request.POST['notes']
            directory.administrator = 'superadmin'

            directory.save()

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

    return render(request, 'directory/show.html', {'directory':directory}) 

def edit(request, id):
    '''
    Edit information about a specific directory
    '''
    try:
        directory = Directories.objects.get(id=int(id))
    except:
        raise Http404('Not found')

    return render(request, 'directory/edit.html', {'directory':directory})

def update(request, id):
    '''
    Update a specific directory
    '''
    try:
        if request.method == 'POST':

            directory = Directories.objects.get(id=int(id))
            directory.full_name = request.POST['full_name'].upper()
            directory.gender = request.POST['gender']
            directory.date_of_birth = request.POST['date_of_birth']
            directory.place_of_birth = request.POST['place_of_birth']
            directory.cin = request.POST['cin']
            directory.delivered_on = request.POST['delivered_on']
            directory.delivered_at = request.POST['delivered_at']
            directory.phone = request.POST['phone']
            directory.urgent_phone = request.POST['urgent_phone']
            directory.email = request.POST['email']
            directory.address = request.POST['address']
            directory.function = request.POST['function']
            directory.departement = request.POST['departement']
            directory.date_of_service = request.POST['date_of_service']
            directory.end_of_service = request.POST['end_of_service']
            directory.matricule_number = request.POST['matricule_number']
            directory.state = request.POST['state']
            directory.avatar = 'myavatar'
            directory.notes = request.POST['notes']
            directory.administrator = 'superuser'

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