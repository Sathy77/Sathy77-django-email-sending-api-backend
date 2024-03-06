from rest_framework import serializers
from contactus.models import *

class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'