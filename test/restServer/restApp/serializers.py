from rest_framework import serializers
from .models import RestApp

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestApp
        field = ('title', 'body', 'subtitle')