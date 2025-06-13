from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .ia_interface import gerar_planejamento_com_ia

@api_view(['POST'])
def gerar_planejamento(request):
    dados = request.data

    resultado = gerar_planejamento_com_ia(dados)

    if "erro" in resultado:
        return Response(resultado, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(resultado, status=status.HTTP_200_OK)
