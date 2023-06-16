from rest_framework import serializers
from .models import student_detail
from .models import teacher_detail
from .models import admin_detail

class S_serializer(serializers.ModelSerializer):
    class Meta:
        model = student_detail
        fields = '__all__'

class T_serializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_detail
        fields = '__all__'

class A_serializer(serializers.ModelSerializer):
    class Meta:
        model = admin_detail
        fields = '__all__'