from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import UserDetails
from rest_framework.generics import ListAPIView
from .serializers import UserDetailsSerializer, GetScoreSerializer
import requests
from rest_framework import status, generics
import django_filters, rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

def getScore(rank):
    data = UserDetails.objects.all()
    data = data.order_by('-score')
    cur=1
    score = data[0].score
    for i in range(len(data)):
        if data[i].score != score:
            cur+=1
            score = data[i].score
        if cur == rank:
            return data[i].score
            

class UserDetailsList(ListAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['score', 'name']
    filterset_fields = ['score', 'name']

    def post(self, request, format=None):
        serializer = GetScoreSerializer(data=request.data)
        if serializer.is_valid():
            rank = serializer.data['rank']
            score = getScore(rank = rank)
            queryset = UserDetails.objects.filter(score=score)
            serialisedData = UserDetailsSerializer(queryset, many=True)
            return Response(serialisedData.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AscedingUserList(ListAPIView):
    queryset = UserDetails.objects.all().order_by('score','name')
    serializer_class = UserDetailsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['score', 'name']
    filterset_fields = ['score', 'name']

class DescendingUserList(ListAPIView):
    queryset = UserDetails.objects.all().order_by('-score','name')
    serializer_class = UserDetailsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['score', 'name']
    filterset_fields = ['score', 'name']
