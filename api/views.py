from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def register(request):
    return Response('Teste')
