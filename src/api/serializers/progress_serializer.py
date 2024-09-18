from rest_framework import serializers
from progress.models.progress_model import ProgressModel


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressModel
        fields=['id','user', 'program', 'date', 'performance_notes']