from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student

        # fields=['name','id']
        fields="__all__"
        # exclude=['age']

    def validate(self,data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'Underage'})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'No numeric name.'})
        
        return data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category']      


class BookSerializer(serializers.ModelSerializer):
    category_name=CategorySerializer()
    class Meta:
        model=Book
        fields="__all__"  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=['username','password']

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user
