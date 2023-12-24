from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def apiView(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)

    return Response({'status':200,'students':serializer.data})

@api_view(['POST'])
def Post_View(request):
    data=request.data
    serializer=StudentSerializer(data=data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':404,'message':'Not found'})

    serializer.save()
    return Response({'status':200,'message':serializer.data})

@api_view(['PUT'])
def Put_view(request):
    data=request.data
