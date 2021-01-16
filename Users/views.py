from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib import messages
from .forms import UserRegisterForm
from .models import CustomUser,Student,Sheet,worksheet, Alum_Detail
from .serializers import CustomUserSerializer,StuidentSerializer,SheetSerializer,worksheetSerializer,Alum_DetailSerializer
from rest_framework.decorators import api_view

def register(request):    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@api_view(['GET'])
def api(request):
    if request.method=='GET':
        obj1=CustomUser.objects.all()
        serializer=CustomUserSerializer(obj1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api1(request):
    if request.method=='GET':
        obj1=Sheet.objects.all()
        serializer=SheetSerializer(obj1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api2(request):
    if request.method=='GET':
        obj1=Student.objects.all()
        serializer=StuidentSerializer(obj1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api3(request):
    if request.method=='GET':
        obj1=Alum_Detail.objects.all()
        serializer=Alum_DetailSerializer(obj1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api4(request):
    if request.method=='GET':
        obj1=worksheet.objects.all()
        serializer=worksheetSerializer(obj1,many=True)
        return Response(serializer.data)