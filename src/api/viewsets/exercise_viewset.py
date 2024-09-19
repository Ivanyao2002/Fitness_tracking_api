from rest_framework import viewsets
from ..serializers.exercise_serializer import ExerciseSerializer
from exercise.models.exrcise_model import ExerciseModel
from rest_framework import status
from rest_framework.response import Response

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
