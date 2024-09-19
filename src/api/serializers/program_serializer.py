from rest_framework import serializers
from program.models.program_model import ProgramModel


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramModel
        fields = ['id', 'user', 'level', 'starting', 'sets']
