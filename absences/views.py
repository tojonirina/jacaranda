from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

from .models import Absence
from directories.models import Directory

class AbsenceView():

    # Get the home page of absence
    def index(request):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            absences = Absence.objects.raw('SELECT * FROM absences a INNER JOIN directories d ON a.directory_id = d.id')
            directories = Directory.objects.all()
        except:
            return HttpResponse("Server or DB error", status=500)

        return render(request, "absences/home.html", {'absences':absences, 'directories':directories})

    # Show all information of a specific absence
    def show(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try: 
            # absence = Absences.objects.raw('SELECT * FROM absences a INNER JOIN directories d ON a.directory_id = d.id AND a.id = 1')
            absence = Absence.objects.get(id=id)
        except Absence.DoesNotExist:
            return HttpResponse("Absence not found", status=404)
            
        return render(request, "absences/show.html", {'absence':absence})

    # Store a new absence request
    def store(request):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            if request.method == 'POST':

                newAbsence = Absence()
                newAbsence.directory_id = request.session.get('current_user_id')
                newAbsence.types = request.POST['types']
                newAbsence.begin_date = request.POST['begin_date']
                newAbsence.end_date = request.POST['end_date']
                newAbsence.interim = request.POST['interim']
                newAbsence.interim_contact = request.POST['interim_contact']
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

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        absence = get_object_or_404(Absence, pk=id)

        return render(request, "absences/edit.html", {'absence':absence})

    # Update a specific absence
    def update(request, id):

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            if request.method == 'POST':

                absence = Absence.objects.get(id=id)
                absence.types = request.POST['types']
                absence.begin_date = request.POST['begin_date']
                absence.end_date = request.POST['end_date']
                absence.interim = request.POST['interim']
                absence.interim_contact = request.POST['interim_contact']
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

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        try:
            if request.method == 'POST':

                newAbsence = Absence.objects.get(id=id)
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

         # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')
            
        try:
            absences = Absence.objects.all()
        except:
            return HttpResponse("Server error", status=500)
        
        return render(request, "absences/reporting.html", {'absences':absences})


    