from django.urls import path, re_path, include
from .views import AbsenceView

app_name = "absences"

urlpatterns = [
    path('', AbsenceView.home, name="absence_home"),
    path('store/', AbsenceView.store, name="store_absence"),
    path('<int:id>/', AbsenceView.show, name="show_absence"),
    path('edit/<int:id>/', AbsenceView.edit, name="edit_absence"),
    path('update/<int:id>/', AbsenceView.update, name="update_absence"),
    path('revoke/<int:id>/', AbsenceView.revoke, name="revoke_absence"),
    path('reportings/', AbsenceView.reporting, name="reporting_absence"),
]