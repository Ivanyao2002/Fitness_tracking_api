from rest_framework import viewsets

from api.serializers.exercise_serializer import ExerciseSerializer
from exercise.models.exrcise_model import ExerciseModel

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer
