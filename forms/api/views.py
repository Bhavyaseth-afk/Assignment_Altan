from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from .serializers import InfoSerializer

# Create your views here.
class InformationList(APIView):
    
   
    queryset=InfoModel.objects.all()
    serializer_class= InfoSerializer
    def get(self,request,format=None):
        info=InfoModel.objects.all()
        serializer= InfoSerializer(info,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
            serializer=InfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status.HTTP_201_CREATED) 
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
          
