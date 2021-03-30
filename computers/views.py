from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Computers
from datetime import datetime
from directories.models import Directories

def home(request):
    """
    Get computer home page and display all computer
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
                newComputer.reference = request.POST['reference']
                newComputer.description = request.POST['description']
                newComputer.state = request.POST['state']
                newComputer.mark = request.POST['mark']
                newComputer.os = request.POST['os']
                newComputer.category = request.POST['category']
                newComputer.assigned_to = request.POST['assigned_to']
                newComputer.assigned_at = datetime.now()
                newComputer.save()
            else:
                newComputer = Computers()
                newComputer.name = request.POST['name']
                newComputer.reference = request.POST['reference']
                newComputer.description = request.POST['description']
                newComputer.state = request.POST['state']
                newComputer.mark = request.POST['mark']
                newComputer.os = request.POST['os']
                newComputer.category = request.POST['category']
                newComputer.save()
        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        return HttpResponse('Server error', status=500)

    return redirect('computers:computer_home')

def show(request, id):
    """
    Show all information of a specific computer
    :param id:
    """
    try:
        computer = Computers.objects.get(id=int(id))
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'computer/show.html', {'computer': computer})

def edit(request, id):
    """
    Get page to edit the information of a specific computer
    :param id:
    """
    try:
        computer = Computers.objects.get(id=int(id))
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'computer/edit.html', {'computer': computer})

def update(request, id):
    """
    Update the information of a computer
    :return redirect to show page:
    """
    try:
        if request.method == 'POST':
            if len(request.POST['assigned_to']) > 5:
                newComputer = Computers.objects.get(id=int(id))
                newComputer.name = request.POST['name']
                newComputer.reference = request.POST['reference']
                newComputer.description = request.POST['description']
                newComputer.state = request.POST['state']
                newComputer.mark = request.POST['mark']
                newComputer.os = request.POST['os']
                newComputer.category = request.POST['category']
                newComputer.assigned_to = request.POST['assigned_to']
                newComputer.assigned_at = datetime.now()
                newComputer.save()
            else:
                newComputer = Computers.objects.get(id=int(id))
                newComputer.name = request.POST['name']
                newComputer.reference = request.POST['reference']
                newComputer.description = request.POST['description']
                newComputer.state = request.POST['state']
                newComputer.mark = request.POST['mark']
                newComputer.os = request.POST['os']
                newComputer.category = request.POST['category']
                newComputer.save()
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