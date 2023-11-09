
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import RotaSerializer
from django.http import JsonResponse
from .models import Rota

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

    