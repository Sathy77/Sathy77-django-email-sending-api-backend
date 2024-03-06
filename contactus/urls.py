from django.urls import path
from contactus import views

urlpatterns = [
    path('', views.addcontactus, name='add-contact-us'),
]
