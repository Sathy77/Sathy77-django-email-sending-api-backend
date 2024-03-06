from django.contrib import admin
from estimateproject.models import *

admin.site.register([
    Userdetails,
    Estimateproject,
    Challenge,
    Alreadyhave,
    Timeframe
])
