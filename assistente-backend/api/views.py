from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlanejamentoRequestSerializer
from .ia_interface import gerar_planejamento_com_ia

@api_view(['POST'])
def gerar_planejamento(request):
    serializer = PlanejamentoRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    dados = serializer.validated_data
    planejamento = gerar_planejamento_com_ia(dados)

    if "erro" in planejamento:
        return Response(planejamento, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(planejamento, status=status.HTTP_200_OK)

