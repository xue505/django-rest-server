from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """ Test api method """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ GET
        return message, an_apiview """

        an_apiview = [
            'bla bla bla',
            'put, get, post, patch, delete'
        ]

        return Response({'message' : 'Hello!',
                         'an_apiview' : an_apiview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)