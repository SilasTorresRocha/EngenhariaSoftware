from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .ia_interface import gerar_planejamento_semana

@api_view(['POST'])
def gerar_planejamento(request):
    dados = request.data

    resultado = gerar_planejamento_semana(dados)

    if "erro" in resultado:
        return Response(resultado, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(resultado, status=status.HTTP_200_OK)
