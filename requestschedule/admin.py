from django.contrib import admin
from requestschedule.models import *

admin.site.register([Userdetails, Requestschedule, Budgetdetails])
