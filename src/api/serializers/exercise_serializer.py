from rest_framework import serializers

from exercise.models.exrcise_model import ExerciseModel


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields= ['id','level', 'name', 'target_area', 'duration', 'repetition', 'description']