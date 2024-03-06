from django.urls import path
from requestschedule import views

urlpatterns = [
    path('', views.addrequestschedule, name='add-request-schedule'),
]
