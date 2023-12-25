from django.shortcuts import render,get_object_or_404
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

@api_view(['PATCH'])
def Update_View(request,id):
    data=request.data
    student_obj = get_object_or_404(Student, id=id)
    serializer=StudentSerializer(student_obj,data=data,partial=True)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':400,'msg':'no such datas'})
    
    serializer.save()
    return Response({'status':200,'message':serializer.data})

@api_view(['DELETE'])
def Delete_View(request,id):
    try:
        student_obj=get_object_or_404(Student,id=id)
        student_obj.delete()
        return Response({'status':400,'message':'Deleted'})
    

    except:
        
  
        return Response({'status':200,'message':'Cannot delete'})

