from django.urls import path
from ride.views import *
app_name='anything'

urlpatterns=[
    path('auto/',auto,name='auto'),
    path('car/',car,name='car'),
]