from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Session

class Session_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
