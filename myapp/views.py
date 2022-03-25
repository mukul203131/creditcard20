from django.shortcuts import render
from itsdangerous import Serializer
from .models import Creditcard
from rest_framework import generics
from .serializers import CreditcardSerializer
# Create your views here.

class CreditcardList(generics.ListCreateAPIView):
    queryset = Creditcard.objects.all()
    serializer_class = CreditcardSerializer