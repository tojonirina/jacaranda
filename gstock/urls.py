from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='login_page'),
    path('index/', views.index, name='index_page'),
    path('default/', views.index, name='default_page'),
    path('users/', include('users.urls')),
    path('materials/', include('materials.urls')),
    path('directories/', include('directories.urls')),
    path('computers/', include('computers.urls')),
    path('absences/', include('absences.urls'))
]
