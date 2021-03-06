from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializers
from .models import Post


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

