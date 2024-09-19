from rest_framework import serializers
from program.models.routine_model import RoutineModel


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineModel
        fields=['id','level', 'target_area', 'exercices']