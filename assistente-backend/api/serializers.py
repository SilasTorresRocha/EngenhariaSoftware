from rest_framework import serializers
from .models import Usuario

class HorarioMateriaSerializer(serializers.Serializer):
    materia = serializers.CharField()
    horario = serializers.RegexField(
        regex=r'^\d{2}:\d{2}-\d{2}:\d{2}$',
        error_messages={"invalid": "Formato deve ser HH:MM-HH:MM"}
    )

class DiasDaSemanaSerializer(serializers.Serializer):
    Segunda = HorarioMateriaSerializer(many=True)
    Terça = HorarioMateriaSerializer(many=True)
    Quarta = HorarioMateriaSerializer(many=True)
    Quinta = HorarioMateriaSerializer(many=True)
    Sexta = HorarioMateriaSerializer(many=True)
    Sábado = HorarioMateriaSerializer(many=True)
    Domingo = HorarioMateriaSerializer(many=True)

class PlanejamentoRequestSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    horarios = serializers.DictField()
    hobbies = serializers.ListField(child=serializers.CharField(), required=False)
    observacoes = serializers.CharField(required=False, allow_blank=True)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome']

class ProvaSerializer(serializers.Serializer):
    materia = serializers.CharField()
    data = serializers.DateField()
    descricao = serializers.CharField()

class TrabalhoSerializer(serializers.Serializer):
    materia = serializers.CharField()
    data_entrega = serializers.DateField()
    descricao = serializers.CharField()

class ProvasTrabalhosRequestSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    provas = ProvaSerializer(many=True)
    trabalhos = TrabalhoSerializer(many=True)


class ProvaResponseSerializer(serializers.Serializer):
    materia = serializers.CharField()
    data = serializers.DateField()
    descricao = serializers.CharField()

class TrabalhoResponseSerializer(serializers.Serializer):
    materia = serializers.CharField()
    data_entrega = serializers.DateField()
    descricao = serializers.CharField()

class SincronizacaoConsultaResponseSerializer(serializers.Serializer):
    provas = ProvaResponseSerializer(many=True)
    trabalhos = TrabalhoResponseSerializer(many=True)

class UsuarioConsultaSerializer(serializers.Serializer):
    usuario = serializers.CharField()