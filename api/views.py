from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mysite.models import posts
from .serializers import PostsSerializer
 
# Create your views here.


@api_view(['GET'])
def posts_serializer(request):
    post = posts.objects.all()
    serializer = PostsSerializer(post,many=True)
    return Response(serializer.data,status=200)