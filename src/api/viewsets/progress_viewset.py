from rest_framework import viewsets
from progress.models.progress_model import ProgressModel
from api.serializers.progress_serializer import ProgressSerializer



class ProgressViewSet(viewsets.ModelViewSet):

    serializer_class = ProgressSerializer
    queryset = ProgressModel.objects.all()
