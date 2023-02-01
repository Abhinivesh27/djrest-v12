
from rest_framework import serializers, fields
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id','name','cc','brand']