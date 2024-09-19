from rest_framework import viewsets
from ..serializers.routine_serializer import RoutineSerializer
from program.models.routine_model import RoutineModel
from rest_framework import status
from rest_framework.response import Response


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = RoutineModel.objects.all()
    serializer_class = RoutineSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



