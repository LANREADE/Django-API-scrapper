from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Advocates
from . serializers import AdvocateSerializer
from django.db.models import Q

from base import serializers

@api_view(['GET'])
def endpoint(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET' , 'POST'])
def advocate(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocates.objects.filter(Q(username__icontains = query )| Q(bio__icontains =query))
        serializer = AdvocateSerializer(advocates, many= True)
        return Response(serializer.data)

    if request.method == 'POST':
        advocates = Advocates.objects.create (
            username = request.data['username'],
            bio = request.data['bio'])

        serializers = AdvocateSerializer(advocates , many= False )
        return Response(serializers.data)

class AdvocatesDetails(APIView):
    def get(self, request, username):
        advocates = Advocates.objects.get(username= username)
        serializer = AdvocateSerializer(advocates , many= False )
        return Response(serializer.data)

    def put(self, request, username):
        advocates.username = request.data['username']
        advocates.bio = request.data['bio']

        advocates.save()
        serializers = AdvocateSerializer(advocates , many=False )
        return Response(serializers.data)





# @api_view(['GET' , 'PUT', 'DELETE'])
# def advocate_list(request, username ):
#     advocates = Advocates.objects.get(username= username)

#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocates , many= False )
#         return Response(serializer.data)

#     if request.method == "PUT":
#         advocates.username = request.data['username']
#         advocates.bio = request.data['bio']

#         advocates.save()
#         serializers = AdvocateSerializer(advocates , many= False )
#         return Response(serializers.data)

#     if request.method == "DELETE":
#         advocates.delete()
#         return Response("user was deleted from the main server")







