from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import myImageClass
from .serializers import myImageClassSerializer

# Create your views here.
class imageList(APIView):
    def get(self, request):
        imagel = myImageClass.objects.all()
        serializer = myImageClassSerializer(imagel, many = True)
        return Response(serializer.data)

    def post(self):
        serializer = MyImageModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    