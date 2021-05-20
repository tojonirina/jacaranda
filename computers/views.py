from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from .models import Computers
from directories.models import Directory

class ComputerView:

    # Get computer home page and display all computer
    def index(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            computers = Computers.objects.all()
            directories = Directory.objects.raw('SELECT id, full_name FROM directories WHERE full_name NOT IN (SELECT assigned_to FROM computers)')

        except:
            return HttpResponse('Serveror DB error', status=500)

        return render(request, 'computer/home.html', {'computers':computers, 'directories':directories})

    # Store a computer
    def store(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

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
                    newComputer.assigned_at = timezone.now()
                    newComputer.fournissor = request.POST['fournissor']
                    newComputer.fournissor_contact = request.POST['fournissor_contact']
                    newComputer.description = request.POST['description']
                    newComputer.administrator = 'superuser'
                    newComputer.save()

                    messages.success(request, 'Computer added successfully and assigned to {}'.format(request.POST['assigned_to']))

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

                    messages.success(request, 'Computer added successfully')

            else:
                return HttpResponse('Forbidden request', status=403)
                
        except:
            return HttpResponse('Server or DB error', status=500)

        return redirect('computers:computer_home')

    #  Show all information of a specific computer
    def show(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            computer = Computers.objects.get(id=int(id))
        except:
            return HttpResponse('Server or DB error', status=500)

        return render(request, 'computer/show.html', {'computer': computer})

    # Get page to edit the information of a specific computer
    def edit(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            computer = Computers.objects.get(id=int(id))
            directories = Directory.objects.raw('SELECT id, full_name FROM directories WHERE full_name NOT IN (SELECT assigned_to FROM computers)')
        except Computers.DoesNotExist:
            return HttpResponse('Computer not found', status=404)

        return render(request, 'computer/edit.html', {'computer': computer,'directories':directories})

    # Update the information of a computer
    def update(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')
            
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
                computer.assigned_at = timezone.now()
                computer.fournissor = request.POST['fournissor']
                computer.fournissor_contact = request.POST['fournissor_contact']
                computer.description = request.POST['description']
                computer.save()

                if len(request.POST['assigned_to']) > 5:
                    messages.success(request, 'Computer added successfully and assigned to {}'.format(request.POST['assigned_to']))
                else:
                    messages.success(request, 'Computer added successfully')
            else:
                return HttpResponse('Forbidden request', status=403)
        except:
            return HttpResponse('Server or DB error', status=500)

        return redirect('computers:show_computer', id)
