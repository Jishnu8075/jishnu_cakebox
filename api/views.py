from django.shortcuts import render

from rest_framework.response import responses
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.views import APIView
from rest_framework import generics

from cakeoperations.models import *
from api.serializers import *

# Create your views here.

class UserCreationView(generics.ListCreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
   
class CakeView(ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Cakes.objects.all()
        serializer=CakeSerializer(qs,many=True)
        return render(data=serializer.data)

