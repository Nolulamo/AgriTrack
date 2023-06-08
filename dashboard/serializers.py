from rest_framework import serializers
from .models import Nutrient

class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ('nitrogen', 'phosphorus', 'potassiun', 'pH', 'ec', 'moisture', 'temperature')