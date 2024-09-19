from rest_framework import viewsets
from exercise.models.exercise_model import ExerciseModel
from api.serializers.exercise_serializer import ExerciseSerializer



class ExerciseViewSet(viewsets.ModelViewSet):

    serializer_class = ExerciseSerializer
    queryset = ExerciseModel.objects.all()
