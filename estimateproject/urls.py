from django.urls import path
from estimateproject import views

urlpatterns = [
    path('', views.addestimateproject, name='add-estimate-project'),
]
