from rest_framework import serializers
from progress.models.progress_model import ProgressModel
from user.models.custom_user_model import CustomUserModel
from program.models.program_model import ProgramModel
from exercise.models.exercise_model import ExerciseModel


class ProgressSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=CustomUserModel.objects.all())
    program = serializers.SlugRelatedField(slug_field='slug', queryset=ProgramModel.objects.all(), allow_null=True)
    exercise = serializers.SlugRelatedField(slug_field='slug', queryset=ExerciseModel.objects.all())
    class Meta:
        model = ProgressModel
        fields = ['id', 'user', 'program', 'exercise', 'date', 'slug']
        read_only_fields = ['id', 'date', 'slug']