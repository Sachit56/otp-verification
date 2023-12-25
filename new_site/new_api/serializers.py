from rest_framework import serializers
from . models import *

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

