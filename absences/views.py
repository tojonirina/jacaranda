from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

from .models import Absences
from directories.models import Directory

class AbsenceView():

    # Get the home page of absence
    def index(request):
        try:
            absences = Absences.objects.raw('SELECT * FROM absences a INNER JOIN directories d ON a.directory_id = d.id')
            directories = Directory.objects.all()
        except:
            return HttpResponse("Server or DB error", status=500)

        return render(request, "absences/home.html", {'absences':absences, 'directories':directories})

    # Show all information of a specific absence
    def show(request, id):
        try: 
            # absence = Absences.objects.raw('SELECT * FROM absences a INNER JOIN directories d ON a.directory_id = d.id AND a.id = 1')
            absence = Absences.objects.get(id=id)
        except Absences.DoesNotExist:
            return HttpResponse("Absence not found", status=404)
            
        return render(request, "absences/show.html", {'absence':absence})

    # Store a new absence request
    def store(request):
        try:
            if request.method == 'POST':

                newAbsence = Absences()
                newAbsence.directory_id = 1
                newAbsence.types = request.POST['types']
                newAbsence.begin_date = request.POST['begin_date']
                newAbsence.end_date = request.POST['end_date']
                newAbsence.interim = request.POST['interim']
                newAbsence.reasons = request.POST['reasons']
                newAbsence.justificative = request.POST['justificative']

                newAbsence.save()

                messages.success(request, 'Your request is sented to your responsable')
                
            else:
                return HttpResponse("Forbidden request", status=403)

        except:
            return HttpResponse("Server or DB error", status=500)
        
        return redirect("absences:absence_home")

    # Get the edit page of a specific absence
    def edit(request, id):

        absence = get_object_or_404(Absences, pk=id)

        return render(request, "absences/edit.html", {'absence':absence})

    # Update a specific absence
    def update(request, id):
        try:
            if request.method == 'POST':

                absence = Absences.objects.get(id=id)
                absence.types = request.POST['types']
                absence.begin_date = request.POST['begin_date']
                absence.end_date = request.POST['end_date']
                absence.interim = request.POST['interim']
                absence.reasons = request.POST['reasons']
                absence.justificative = request.POST['justificative']
                absence.updated_at = timezone.now()

                absence.save()

                messages.warning(request, 'Your request is updated, you cannot update it')

            else:
                return HttpResponse("Forbidden request", status=403)

        except:
            return HttpResponse("Server error", status=500)
        
        return redirect("absences:show_absence", id)
        
    # Revoke a specific absence request
    def revoke(request, id):
        try:
            if request.method == 'POST':

                newAbsence = Absences.objects.get(id=id)
                newAbsence.status = 3

                newAbsence.save()

                messages.error(request, 'Your request is canceled')
                
            else:
                return HttpResponse("Forbidden request", status=403)

        except:
            return HttpResponse("Server or DB error", status=500)
        
        return redirect("absences:absence_home")

    # Show all stats about all absence
    def reporting(request):
        try:
            absences = Absences.objects.all()
        except:
            return HttpResponse("Server error", status=500)
        
        return render(request, "absences/reporting.html", {'absences':absences})


    