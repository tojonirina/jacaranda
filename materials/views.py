from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Material, MouvmentHistory
from django.contrib import messages

from math import fabs

class MaterialView:

    # Get material home page
    def index(request):
        try: 
            materials = Material.objects.all()
        except:
            raise Http404('Not found')
        
        return render(request, 'material/home.html', {'materials': materials})

    # Show all information about a specific material
    def show(request, id): 
        try:
            maretial = Material.objects.get(id=int(id))
        except:
            raise Http404('Page not found')

        return render(request, 'material/show.html', {'material':maretial})

    # Store a material in stock
    def store(request):
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
                    material.administrator = 'superadmin'

                    material.save()

                    messages.success(request, 'Product added successfully')

                    # mouvment = MouvmentHistory()
                    # mouvment.title = request.POST['title']
                    # mouvment.description = request.POST['description']
                    # mouvment.quantity = fabs(int(request.POST['quantity']))
                    # mouvment.unity = request.POST['unity']
                    # mouvment.state = request.POST['state']
                    # mouvment.administrator = 'superadmin'
                    # mouvment.types = 'entry'

                    # mouvment.save()

                elif request.POST['old_product'] != '':

                    material = Materials.objects.get(id=int(request.POST['old_product']))
                    material.quantity += int(request.POST['quantity'])

                    material.save()
                    
                    # mouvment = MouvmentHistory()
                    # mouvment.product_id = request.POST['old_product']
                    # mouvment.note = request.POST['note']
                    # mouvment.quantity = fabs(int(request.POST['quantity']))
                    # mouvment.unity = request.POST['unity']
                    # mouvment.state = request.POST['state']
                    # mouvment.types = 'entry'
                    # mouvment.administrator = 'superadmin'

                    # mouvment.save()
                else:
                        return HttpResponse('umm error', status=500)
            else:
                return HttpResponse('Unauthorized', status=401)
                
        except:
            return HttpResponse('Server error', status=500)
        
        return redirect('materials:material_home')

    # Update a materiel information
    def update(request, id):
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

                material.save()

                messages.success(request, 'Product updated successfully')
            else:
                return HttpResponse('Unauthorized', status=401)
                
        except:
            return HttpResponse('Server error', status=500)
        
        return redirect('materials:show_material', id)

    # Show takeout form
    def getTakeOut(request):
        try: 
            materials = Material.objects.all()
        except:
            raise Http404('Connection error')

        return render(request, 'material/takeout.html', {'materials':materials})

    # Take out a materiel in stock
    def postTakeOut(request):
        try:
            if request.method == 'POST':
                
                material = Material.objects.get(id=int(request.POST['material']))
                material.quantity -= fabs(int(request.POST['quantity']))
                material.save()

                mouvment = MouvmentHistory()
                mouvment.product_id = int(request.POST['material'])
                mouvment.note = request.POST['note']
                mouvment.quantity = fabs(int(request.POST['quantity']))
                mouvment.unity = request.POST['unity']
                mouvment.state = request.POST['state']
                mouvment.administrator = 'superadmin'
                mouvment.types = 'takeout'
                mouvment.save()

                messages.success(request, 'Product take out successfully')
                
            else:
                return HttpResponse('unauthorized', status=401)
                
        except:
            return HttpResponse('Server error', status=500)
        
        return redirect('materials:material_home')
        
    #  Edit a materiel information
    def edit(request, id):
        try:
            maretial = Material.objects.get(id=int(id))
        except:
            raise Http404('Page not found')

        return render(request, 'material/edit.html', {'material':maretial})

    #  Get all mouvment history
    def history(request):
        try:
            history = MouvmentHistory.objects.all()
        except:
            return HttpResponse('Connection error', status=500)
            
        return render(request, 'material/history.html', {'history':history}) 

    def reporting(request):

        # entryEveryMonth = Materials.objects.raw("SELECT DISTINCT SUM(quantity) FROM materials WHERE created_at BETWEEN '01/01/2021' AND '31/01/2021' GROUP BY title")
        values = [12, 43, 22, 52, 13, 65, 12, 43, 22, 52, 13, 65]

        return render(request, 'material/reporting.html', {'values':values})