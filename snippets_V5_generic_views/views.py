# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
