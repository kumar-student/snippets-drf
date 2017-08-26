# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import UserSerializer
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from rest_framework import permissions

from permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer