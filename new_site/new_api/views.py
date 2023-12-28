from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
import pandas as pd
from django.conf import settings
import uuid

# Create your views here.
class StudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        print(request.user)

        return Response({'status':200,'students':serializer.data})
    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':404,'message':'Not found'})

        serializer.save()
        return Response({'status':200,'message':serializer.data})
    
    def patch(self,request,*args, **kwargs):
        id=kwargs.get("id")
        data=request.data
        student_obj = get_object_or_404(Student, id=id)
        serializer=StudentSerializer(student_obj,data=data,partial=True)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':400,'msg':'no such datas'})
        
        serializer.save()
        return Response({'status':200,'message':serializer.data})

    def delete(self,request,id):
        try:
            student_obj=get_object_or_404(Student,id=id)
            student_obj.delete()
            return Response({'status':400,'message':'Deleted'})
    

        except:
        
  
            return Response({'status':200,'message':'Cannot delete'})


class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentIdGeneric(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field='id'

class GeneratePdf(APIView):
    def get(self,request):

        return Response({'status':200})

@api_view(['GET'])
def BookView(request):
    Book_obj=Book.objects.all()
    serializer=BookSerializer(Book_obj,many=True)

    return Response({'status':200,'message':serializer.data})

class UserView(APIView):
    def post(self,request):
        data=request.data
        
        serializer=UserSerializer(data=data)


        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':400,'message':serializer.errors})
        serializer.save()

        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)


        return Response({'status':200,'message':serializer.data,'refresh':str(refresh),
        'access': str(refresh.access_token)})

class ExcelView(APIView):
    def get(self,request):
        student_obj=Student.objects.all()

        seralizer=StudentSerializer(student_obj,many=True)
        df=pd.DataFrame(seralizer.data)
        print(df)
        df.to_csv(f'public/static/excel/{uuid.uuid4()}.csv',encoding='UTF-8')

        return Response({'status':200})