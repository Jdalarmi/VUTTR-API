from rest_framework import serializers
from api.models import Rota

class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = '__all__'
        
class TagRequestSerializer(serializers.Serializer):
    tag = serializers.CharField(max_length=100)
