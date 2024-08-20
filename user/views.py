from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Customer

@api_view(['POST'])
def create_customer(request):
    username = request.data.get('username')
    password = request.data.get('password')
    name = request.data.get('name')
    mobile_no = request.data.get('mobile_no')

    if not all([username, password, name, mobile_no]):
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password)
        Customer.objects.create(user=user, name=name, mobile_no=mobile_no)
        return Response({"success": "Customer created successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
