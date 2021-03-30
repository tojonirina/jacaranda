from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Materials, MouvmentHistory

from math import fabs

def home(request):
    '''
    Get material home page
    '''
    try: 
        materials = Materials.objects.all()
    except:
        raise Http404('Not found')
    
    return render(request, 'material/home.html', {'materials': materials})

def show(request, id): 
    '''
    Show all information about a specific material
    '''
    try:
        maretial = Materials.objects.get(id=int(id))
    except:
        raise Http404('Page not found')

    return render(request, 'material/show.html', {'material':maretial})

def store(request):
    """
    Store a material in stock
    """
    try:

        if request.method == 'POST':

            if request.POST['title'] != '' and request.POST['description'] != '':

                material = Materials()
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

                mouvment = MouvmentHistory()
                mouvment.title = request.POST['title']
                mouvment.description = request.POST['description']
                mouvment.quantity = fabs(int(request.POST['quantity']))
                mouvment.unity = request.POST['unity']
                mouvment.state = request.POST['state']
                mouvment.administrator = 'superadmin'
                mouvment.types = 'entry'

                material.save()
                mouvment.save()

            elif request.POST['old_product'] != '':

                material = Materials.objects.get(id=int(request.POST['old_product']))
                material.quantity += int(request.POST['quantity'])

                mouvment = MouvmentHistory()
                mouvment.product_id = request.POST['old_product']
                mouvment.note = request.POST['note']
                mouvment.quantity = fabs(int(request.POST['quantity']))
                mouvment.unity = request.POST['unity']
                mouvment.state = request.POST['state']
                mouvment.types = 'entry'
                mouvment.administrator = 'superadmin'

                material.save()
                mouvment.save()
            else:
                    return HttpResponse('umm error', status=500)
        else:
            return HttpResponse('Unauthorized', status=401)
            
    except:
        return HttpResponse('Server error', status=500)
    
    return redirect('material:material_home')

def update(request, id):
    """
    Update a materiel information
    """

def getTakeOut(request):
    try: 
        materials = Materials.objects.all()
    except:
        raise Http404('Connection error')

    return render(request, 'material/takeout.html', {'materials':materials})

def postTakeOut(request):
    """
    Take out a materiel in stock
    """
    try:
        if request.method == 'POST':
            
            material = Materials.objects.get(id=int(request.POST['material']))
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
            
        else:
            return HttpResponse('unauthorized', status=401)
            
    except:
        return HttpResponse('Server error', status=500)
    
    return redirect('material:material_home')
    
def edit(request, id):
    """
    Edit a materiel information
    """
    try:
        maretial = Materials.objects.get(id=int(id))
    except:
        raise Http404('Page not found')

    return render(request, 'material/edit.html', {'material':maretial})

def history(request):
    '''
    Get all takeout history
    '''
    try:
        history = MouvmentHistory.objects.all()
    except:
        return HttpResponse('Connection error', status=500)
        
    return render(request, 'material/history.html', {'history':history}) 

def reporting(request):
    values = [12, 43, 22, 52, 13, 65]
    return render(request, 'material/reporting.html', {'values':values})