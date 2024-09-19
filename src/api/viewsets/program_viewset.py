from rest_framework import viewsets
from program.models.program_model import ProgramModel
from api.serializers.program_serializer import ProgramSerializer



class ProgramViewSet(viewsets.ModelViewSet):

    serializer_class = ProgramSerializer
    queryset = ProgramModel.objects.all()
