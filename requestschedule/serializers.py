from rest_framework import serializers
from requestschedule.models import Userdetails, Requestschedule

class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = ['name', 'phone']

class RequestscheduleSerializer(serializers.ModelSerializer):
    userDetails = UserdetailsSerializer(many=False)
    class Meta:
        model = Requestschedule
        fields = ['service', 'date', 'time', 'budget', 'description', 'userDetails']