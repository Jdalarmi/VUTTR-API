from rest_framework import serializers
from api.models import Rota

class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = '__all__'