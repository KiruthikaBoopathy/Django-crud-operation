from rest_framework import serializers
from crud_app.models import stud_table


class serialdata(serializers.ModelSerializer):
    class Meta:
        model = stud_table
        fields = '__all__'


class getpost(serializers.Serializer):
        name = serializers.CharField()
