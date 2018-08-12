from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

class HelloApiView(APIView):
    """ Test api method """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Получение
        return message, an_apiview """

        an_apiview = [
            'bla bla bla',
            'put, get, post, patch, delete'
        ]

        return Response({'message' : 'Hello!',
                         'an_apiview' : an_apiview})

    def post(self, request):
        """ Создание """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Замена """
        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """ Редактирование """
        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """ Удалить """
        return Response({'method' : 'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'GET',
            'PUT',
            'PATCH'
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """" Create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({"message" : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting an object by its ID """

        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerailizer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')