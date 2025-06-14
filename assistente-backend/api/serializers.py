from rest_framework import serializers

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
    horarios = DiasDaSemanaSerializer()
    hobbies = serializers.ListField(child=serializers.CharField())
    observacoes = serializers.CharField()
