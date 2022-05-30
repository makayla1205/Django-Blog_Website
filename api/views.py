from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/post-list/',
        'Detail View': '/post-detail/<str:pk>/',
        'Create': '/post-create/',
        'Update': '/post-update/<str:pk>/',
        'Delete': '/post-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def apiList(request):
    list = Post.objects.all()
    serializer = PostSerializer(list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def apiCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def apiUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def apiDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Item Successfully Deleted")


