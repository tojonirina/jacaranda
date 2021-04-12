from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Computers
from datetime import datetime
from directories.models import Directories

def home(request):
    """
    Get computer home page and display all computer and all directories
    """
    try:
        computers = Computers.objects.all()
        directories = Directories.objects.all()
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'computer/home.html', {'computers':computers, 'directories':directories})

def store(request):
    """
    Store a computer
    :return redirect to home page:
    """
    try:
        if request.method == 'POST':

            if len(request.POST['assigned_to']) > 5:
                newComputer = Computers()
                newComputer.name = request.POST['name']
                newComputer.serial_number = request.POST['serial_number']
                newComputer.modele = request.POST['modele']
                newComputer.mark = request.POST['mark']
                newComputer.processor = request.POST['processor']
                newComputer.processor_generation = request.POST['processor_generation']
                newComputer.ram = request.POST['ram']
                newComputer.type_of_ram = request.POST['type_of_ram']
                newComputer.os = request.POST['os']
                newComputer.state = request.POST['state']
                newComputer.status = request.POST['status']
                newComputer.category = request.POST['category']
                newComputer.assigned_to = request.POST['assigned_to']
                newComputer.assigned_at = datetime.now()
                newComputer.fournissor = request.POST['fournissor']
                newComputer.fournissor_contact = request.POST['fournissor_contact']
                newComputer.description = request.POST['description']
                newComputer.administrator = 'superuser'
                newComputer.save()
            else:
                newComputer = Computers()
                newComputer.name = request.POST['name']
                newComputer.serial_number = request.POST['serial_number']
                newComputer.modele = request.POST['modele']
                newComputer.mark = request.POST['mark']
                newComputer.processor = request.POST['processor']
                newComputer.processor_generation = request.POST['processor_generation']
                newComputer.ram = request.POST['ram']
                newComputer.type_of_ram = request.POST['type_of_ram']
                newComputer.os = request.POST['os']
                newComputer.state = request.POST['state']
                newComputer.status = request.POST['status']
                newComputer.category = request.POST['category']
                newComputer.assigned_to = ''
                newComputer.fournissor = request.POST['fournissor']
                newComputer.fournissor_contact = request.POST['fournissor_contact']
                newComputer.description = request.POST['description']
                newComputer.administrator = 'superuser'
                newComputer.save()
        else:
            return HttpResponse('Unauthorized', status=401)
            
    except:
        return HttpResponse('Server error', status=500)

    return redirect('computers:computer_home')

def show(request, id):
    """
    Show all information of a specific computer
    :param id: integer
    """
    try:
        computer = Computers.objects.get(id=int(id))
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'computer/show.html', {'computer': computer})

def edit(request, id):
    """
    Get page to edit the information of a specific computer
    :param id: integer
    """
    try:
        computer = Computers.objects.get(id=int(id))
        directories = Directories.objects.all()
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'computer/edit.html', {'computer': computer,'directories':directories})

def update(request, id):
    """
    Update the information of a computer
    :return redirect to show page:
    """
    try:
        if request.method == 'POST':
            computer = Computers.objects.get(id=int(id))
            computer.name = request.POST['name']
            computer.serial_number = request.POST['serial_number']
            computer.modele = request.POST['modele']
            computer.mark = request.POST['mark']
            computer.processor = request.POST['processor']
            computer.processor_generation = request.POST['processor_generation']
            computer.ram = request.POST['ram']
            computer.type_of_ram = request.POST['type_of_ram']
            computer.os = request.POST['os']
            computer.state = request.POST['state']
            computer.status = request.POST['status']
            computer.category = request.POST['category']
            computer.assigned_to = request.POST['assigned_to']
            computer.assigned_at = datetime.now()
            computer.fournissor = request.POST['fournissor']
            computer.fournissor_contact = request.POST['fournissor_contact']
            computer.description = request.POST['description']
            computer.save()
        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        return HttpResponse('Server error', status=500)

    return redirect('computers:show_computer', id)

def delete(request, id):
    """
    Delete a specific computer
    :param id:
    """
    try:
        computer = Computers.objects.get(id=int(id))
        computer.delete()
    except:
        return HttpResponse('Server error', status=500)
    return redirect('computers:computer_home')