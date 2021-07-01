from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Material, MouvmentHistory
from django.contrib import messages

from math import fabs

class MaterialView:

    # Get material home page
    def index(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try: 
            materials = Material.objects.all()
        except:
            return HttpResponse('Server or DB error', status=500)
        
        return render(request, 'material/home.html', {'materials': materials})

    # Show all information about a specific material
    def show(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            maretial = Material.objects.get(id=int(id))
        except Material.DoesNotExist:
            raise Http404('Material does not found')

        return render(request, 'material/show.html', {'material':maretial})

    # Store a material in stock
    def store(request):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:

            if request.method == 'POST':

                if request.POST['title'] != '' and request.POST['description'] != '':

                    material = Material()
                    material.title = request.POST['title']
                    material.serial_number = request.POST['serial_number']
                    material.modele = request.POST['modele']
                    material.description = request.POST['description']
                    material.quantity = fabs(int(request.POST['quantity']))
                    material.unity = request.POST['unity']
                    material.state = request.POST['state']
                    material.fournissor = request.POST['fournissor']
                    material.fournissor_contact = request.POST['fournissor_contact']
                    material.administrator = request.session.get('current_user_login')


                    mouvment = MouvmentHistory()
                    mouvment.product_name = request.POST['title']
                    mouvment.description = request.POST['description']
                    mouvment.quantity = fabs(int(request.POST['quantity']))
                    mouvment.unity = request.POST['unity']
                    mouvment.state = request.POST['state']
                    mouvment.administrator = request.session.get('current_user_login')
                    mouvment.types = 'entry'

                    material.save() # save material
                    mouvment.save() # add an history of the mouvement

                    messages.success(request, 'New product added successfully')

                elif int(request.POST['old_product']) > 0:

                    material = Material.objects.get(id=int(request.POST['old_product']))
                    material.quantity += fabs(int(request.POST['quantity']))

                    
                    mouvment = MouvmentHistory()
                    mouvment.product_id = request.POST['old_product']
                    mouvment.note = request.POST['note']
                    mouvment.quantity = fabs(int(request.POST['quantity']))
                    mouvment.unity = request.POST['unity']
                    mouvment.state = request.POST['state']
                    mouvment.types = 'entry'
                    mouvment.administrator = request.session.get('current_user_login')

                    material.save() # save material
                    mouvment.save() # add an history of the mouvement

                    messages.success(request, 'Product added successfully')

                else:
                    messages.error(request, 'Please check all fields')
            else:
                return HttpResponse('Forbidden request', status=403)
                
        except:
            return HttpResponse('Server error', status=500)
        
        return redirect('materials:material_home')

    # Update a materiel information
    def update(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:

            if request.method == 'POST':

                material = Material.objects.get(id=int(id))
                material.title = request.POST['title']
                material.serial_number = request.POST['serial_number']
                material.modele = request.POST['modele']
                material.description = request.POST['description']
                material.quantity = request.POST['quantity']
                material.unity = request.POST['unity']
                material.state = request.POST['state']
                material.fournissor = request.POST['fournissor']
                material.fournissor_contact = request.POST['fournissor_contact']

                mouvment = MouvmentHistory()
                mouvment.product_name = request.POST['title']
                mouvment.description = request.POST['description']
                mouvment.quantity = fabs(int(request.POST['quantity']))
                mouvment.unity = request.POST['unity']
                mouvment.state = request.POST['state']
                mouvment.administrator = request.session.get('current_user_login')
                mouvment.types = 'edit'

                material.save()
                mouvment.save()

                messages.success(request, 'Product updated successfully')

            else:
                return HttpResponse('Forbidden request', status=403)
                
        except:
            return HttpResponse('Server or DB error', status=500)
        
        return redirect('materials:show_material', id)

    # Show takeout form
    def getTakeOut(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('materials:material_home')

        try: 
            materials = Material.objects.all()
        except:
            return HttpResponse('Server or DB error', status=500)

        return render(request, 'material/takeout.html', {'materials':materials})

    # Take out a materiel in stock
    def postTakeOut(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to do this action')
                return redirect('materials:material_home')

        try:
            if request.method == 'POST':
                
                material = Material.objects.get(id=int(request.POST['material']))
                material.quantity -= fabs(int(request.POST['quantity']))

                mouvment = MouvmentHistory()
                mouvment.product_id = int(request.POST['material'])
                mouvment.note = request.POST['note']
                mouvment.quantity = fabs(int(request.POST['quantity']))
                mouvment.unity = request.POST['unity']
                mouvment.state = request.POST['state']
                mouvment.administrator = request.session.get('current_user_login')
                mouvment.types = 'takeout'
                
                material.save()
                mouvment.save()

                messages.success(request, 'Product takeouted successfully')
                
            else:
                return HttpResponse('Forbidden request', status=403)
                
        except:
            return HttpResponse('Server or DB error', status=500)
        
        return redirect('materials:material_home')
        
    #  Edit a materiel information
    def edit(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            maretial = Material.objects.get(id=int(id))
        except Material.DoesNotExist:
            raise Http404('Material does not found')

        return render(request, 'material/edit.html', {'material':maretial})

    #  Get all mouvment history
    def history(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            history = MouvmentHistory.objects.raw('SELECT * FROM mouvment_history h LEFT JOIN materials m ON h.product_id = m.id ORDER BY h.created_at DESC')
        except:
            return HttpResponse('Server or DB error', status=500)
            
        return render(request, 'material/history.html', {'history':history}) 

    def reporting(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')
            

        # entryEveryMonth = Materials.objects.raw("SELECT DISTINCT SUM(quantity) FROM materials WHERE created_at BETWEEN '01/01/2021' AND '31/01/2021' GROUP BY title")
        values = [12, 43, 22, 52, 13, 65, 12, 43, 22, 52, 13, 65]

        return render(request, 'material/reporting.html', {'values':values})