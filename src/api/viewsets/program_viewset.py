from rest_framework import viewsets
from ..serializers.program_serializer import ProgramSerializer
from program.models.program_model import ProgramModel
from rest_framework import status
from rest_framework.response import Response


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = ProgramModel.objects.all()
    serializer_class = ProgramSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



