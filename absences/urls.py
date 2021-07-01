from django.urls import path
from .views import AbsenceView

app_name = "absences"

urlpatterns = [
    path('', AbsenceView.index, name="absence_home"),
    path('store/', AbsenceView.store, name="store_absence"),
    path('<int:id>/', AbsenceView.show, name="show_absence"),
    path('<int:id>/edit/', AbsenceView.edit, name="edit_absence"),
    path('<int:id>/update/', AbsenceView.update, name="update_absence"),
    path('<int:id>/cancel/', AbsenceView.revoke, name="revoke_absence"),
    path('reportings/', AbsenceView.reporting, name="reporting_absence"),
]

