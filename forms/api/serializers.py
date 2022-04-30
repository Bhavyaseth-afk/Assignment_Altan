from attr import field, fields
from .models import *
from rest_framework import serializers


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=InfoModel
        fields ='__all__'
    