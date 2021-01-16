from rest_framework import serializers
from .models import CustomUser,Student,Sheet,worksheet, Alum_Detail

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

class StuidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sheet
        fields='__all__'

class worksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=worksheet
        fields='__all__'

class Alum_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alum_Detail
        fields='__all__'