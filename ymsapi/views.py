from django.http import JsonResponse
from .models import student_detail
from .models import teacher_detail
from .models import admin_detail
from .serializers import S_serializer
from .serializers import T_serializer
from .serializers import A_serializer
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework import status  

@api_view(['GET', 'POST']) #remove post add delete
def stu_list(request, format=None):

    if request.method == 'GET':
        stu = student_detail.objects.all()
        serializer = S_serializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = S_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        
@api_view (['GET', 'PUT', 'DELETE'])        #add post
def stu_detail(request,  id, format=None):

    try:
        stu =  student_detail.objects .get(pk=id)
    except student_detail.DoesNotExsist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = S_serializer(stu)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = S_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST']) #remove post add delete
def tea_list(request, format=None):

    if request.method == 'GET':
        tea = teacher_detail.objects.all()
        serializer = T_serializer(tea, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = T_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        
@api_view (['GET', 'PUT', 'DELETE'])        #add post
def tea_detail(request,  id, format=None):

    try:
        tea =  teacher_detail.objects .get(pk=id)
    except teacher_detail.DoesNotExsist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = T_serializer(tea)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = T_serializer(tea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST']) #remove post add delete
def adm_list(request, format=None):

    if request.method == 'GET':
        adm = admin_detail.objects.all()
        serializer = A_serializer(adm, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = A_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        
@api_view (['GET', 'PUT', 'DELETE'])        #add post
def adm_detail(request,  id, format=None):

    try:
        adm =  admin_detail.objects .get(pk=id)
    except admin_detail.DoesNotExsist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = A_serializer(adm)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = A_serializer(adm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        adm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)