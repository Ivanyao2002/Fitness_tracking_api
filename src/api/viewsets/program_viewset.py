from rest_framework import viewsets
from api.serializers.program_serializer import ProgramSerializer
from program.models.program_model import ProgramModel


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = ProgramModel.objects.all()
    serializer_class = ProgramSerializer