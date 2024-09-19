from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Avg 
from progress.models.progress_model import ProgressModel
from ..serializers.progress_serializer import ProgressSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = ProgressModel.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated] 
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def advice(self, request):
        progress_queryset = self.get_queryset()

        last_30_days = now().date() - timedelta(days=30)
        recent_progress = progress_queryset.filter(date__gte=last_30_days)

        if not recent_progress.exists():
            advice = "Commencez ou reprenez vos entraînements pour suivre vos progrès."
        else:
            avg_performance_notes = recent_progress.aggregate(Avg('performance_notes'))['performance_notes__avg']
            total_sessions = recent_progress.count()

            if total_sessions < 5:
                advice = "Essayez de suivre un programme plus régulier pour de meilleurs résultats."
            elif avg_performance_notes is not None and avg_performance_notes < 50:
                advice = "Vos performances peuvent être améliorées, essayez d'augmenter la durée ou l'intensité de vos exercices."
            else:
                advice = "Vous faites du bon travail, continuez ainsi !"

        return Response({"advice": advice})
