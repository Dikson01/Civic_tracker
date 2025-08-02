# issues/serializers.py
from rest_framework import serializers
from .models import CivicIssue

class CivicIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CivicIssue
        fields = '__all__'
