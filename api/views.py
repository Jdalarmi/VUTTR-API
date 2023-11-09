
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import RotaSerializer, TagRequestSerializer
from django.http import JsonResponse
from .models import Rota
from rest_framework import status
from rest_framework import filters
from rest_framework import generics


@swagger_auto_schema(method='post', request_body=RotaSerializer)
@api_view(['POST'])
def register(request):
    serializer = RotaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response('Ferramenta cadastrada com sucesso!', status=200)
    else:
        return JsonResponse('Metodo nao permitido', status=405)
    
    
@api_view(['GET'])
def list_all(request):
    skills = Rota.objects.all()
    serializer = RotaSerializer(skills, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='put')
@api_view(['PUT'])
def delete_by_id(request,pk):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    rota = Rota.objects.get(id=pk)

    rota.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='post', request_body=TagRequestSerializer)
@api_view(['POST'])
def search_tag(request):
    serializer =TagRequestSerializer(data=request.data)

    if serializer.is_valid():
        tag = serializer.validated_data.get('tag')
        find_in_tags = Rota.objects.filter(tags__icontains=tag)
        serializer = RotaSerializer(find_in_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Por favor forneça uma string de pesquisa valida'})

