from rest_framework import serializers
from .models import Creditcard

class CreditcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditcard
        fields = '__all__'        