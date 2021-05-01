from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from .models import Directory

class DirectoryView:

    # Get all directories 
    def index(request):
        try:
            directories = Directory.objects.all()
        except:
            return HttpResponse('Server or DB error', status=500)

        return render(request, 'directory/home.html', {'directories':directories})

    # Store a new directory
    def store(request):
        try:
            if request.method == 'POST':

                directory = Directory()
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
                directory.avatar = 'jaca-icon-orange-72x72.png'
                directory.notes = request.POST['notes']
                directory.administrator = 'superadmin'

                directory.save()

                messages.success(request, 'Directory added successfully')

            else:
                return HttpResponse('Forbidden request', status=403)
        except:
            return HttpResponse('Server or DB error', status=500)

        return redirect('directories:directory_home')

    # Show information of an directory
    def show(request, id):
        try:
            directory = Directory.objects.get(id=int(id))
        except Directory.DoesNotExist:
            return HttpResponse('Directory does Not found', status=404)

        return render(request, 'directory/show.html', {'directory':directory}) 

    # Edit information about a specific directory
    def edit(request, id):
        try:
            directory = Directory.objects.get(id=int(id))
        except Directory.DoesNotExist:
            return HttpResponse('Directory does Not found', status=404)

        return render(request, 'directory/edit.html', {'directory':directory})

    # Update information of a specific directory
    def update(request, id):
        try:
            if request.method == 'POST':

                directory = Directory.objects.get(id=int(id))
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
                directory.avatar = 'jaca-icon-orange-72x72.png'
                directory.notes = request.POST['notes']
                directory.administrator = 'superuser'

                directory.save()

                messages.success(request, 'Directory updated successfully')

            else:
                return HttpResponse('Forbidden request', status=403)
        except:
            return HttpResponse('Server or DB error', status=500)

        return redirect('directories:show_directory', id)

    # Delete a directory
    def delete(request, id):
        try:
            if request.method == 'POST':
                directory = Directory.objects.get(id=int(id))
                directory.delete()
                messages.error(request, 'Directory deleted')
            else:
                return HttpResponse('Forbidden request', status=403)
        except Directory.DoesNotExist:
            return HttpResponse('Directory does Not found', status=404)

        return redirect('directories:directory_home')