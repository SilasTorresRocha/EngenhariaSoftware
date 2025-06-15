from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PlanejamentoRequestSerializer
from .ia_interface import gerar_planejamento_com_ia
from .models import Usuario
from .serializers import UsuarioSerializer 

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


class ValidarUsuarioView(APIView):
    def post(self, request):
        username = request.data.get('username')
        if not username:
            return Response({'message': 'Nome de usuário obrigatório.'}, status=400)

        if Usuario.objects.filter(nome=username).exists():
            return Response({'isValid': True}, status=200)
        else:
            return Response({'isValid': False, 'message': 'Usuário não encontrado'}, status=404)

class CriarUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            
            # Verifica se já existe
            if Usuario.objects.filter(nome=nome).exists():
                return Response({'message': 'Usuário já existe'}, status=400)
            
            serializer.save()
            return Response({'message': 'Usuário criado com sucesso'}, status=201)

        return Response(serializer.errors, status=400)

