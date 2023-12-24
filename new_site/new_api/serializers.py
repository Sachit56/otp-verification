from rest_framework import serializers
from . models import Student

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
    
    