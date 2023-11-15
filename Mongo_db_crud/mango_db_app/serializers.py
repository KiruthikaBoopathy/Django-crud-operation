from rest_framework import serializers
from .models import PlacementDetails
from mango_db_app import models

class ass_serial(serializers.ModelSerializer):
    class Meta:
        model = PlacementDetails
        fields = '__all__'


class Candidate(serializers.Serializer):
    candidate_name = serializers.CharField()


class Renamed(serializers.Serializer):
    candidate_name = serializers.CharField()
    re_name = serializers.CharField()