from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)

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
        token_obj, _ =    Token.objects.get_or_create(user=user)

        return Response({'status':200,'message':serializer.data,'token':str(token_obj)})
