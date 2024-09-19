from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Avg 
from progress.models.progress_model import ProgressModel
from ..serializers.progress_serializer import ProgressSerializer
from user.models.custom_user_model import CustomUserModel  

class ProgressViewSet(viewsets.ModelViewSet):

    queryset = ProgressModel.objects.all()
    serializer_class = ProgressSerializer

    def get_queryset(self):

        user_id = self.request.query_params.get('user_id')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset

    def calculate_bmi(self, weight, size):

        height_in_meters = size / 100  # Convertir la taille en mètres
        if height_in_meters > 0:
            bmi = weight / (height_in_meters ** 2)
            return round(bmi, 2)
        return None

    def calculate_performance_score(self, bmi, total_sessions, avg_performance_notes):
      
        score = 0
        
        # Calcul basé sur l'IMC
        if bmi:
            if bmi < 18.5:
                score -= 10  
            elif 18.5 <= bmi <= 24.9:
                score += 10  
            else:
                score -= 5  
        # Calcul basé sur le nombre de sessions
        if total_sessions < 5:
            score -= 10  
        elif total_sessions >= 5:
            score += 10 

        # Calcul basé sur la performance moyenne
        if avg_performance_notes:
            if avg_performance_notes >= 50:
                score += 10  
            else:
                score -= 5  
        return score

    @action(detail=False, methods=['get'])
    def advice(self, request):

        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "L'ID de l'utilisateur est requis"}, status=400)

        # Récupérer les progrès de l'utilisateur
        progress_queryset = self.get_queryset()
        if not progress_queryset.exists():
            return Response({"advice": "Aucun progrès enregistré. Commencez à enregistrer vos performances."})

        # Récupérer les informations de l'utilisateur
        try:
            user = CustomUserModel.objects.get(id=user_id)
        except CustomUserModel.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=404)

        weight = user.weight
        size = user.size
        age = user.age

        # Calculer l'IMC de l'utilisateur
        bmi = self.calculate_bmi(weight, size)

        # Filtrer les progrès récents sur 30 jours
        last_30_days = now().date() - timedelta(days=30)
        recent_progress = progress_queryset.filter(date__gte=last_30_days)

        # Calcul des performances moyennes
        avg_performance_notes = recent_progress.aggregate(Avg('performance_notes'))['performance_notes__avg']
        total_sessions = recent_progress.count()

        # Calculer le score de performance global
        performance_score = self.calculate_performance_score(bmi, total_sessions, avg_performance_notes)

        # Générer des conseils basés sur le score
        if performance_score >= 20:
            advice = "Vous êtes en bonne forme. Continuez ainsi et maintenez une bonne régularité."
        elif 10 <= performance_score < 20:
            advice = "Vous progressez bien, mais vous pourriez améliorer vos performances en augmentant la régularité et l'intensité."
        else:
            advice = "Vos performances sont faibles. Essayez d'augmenter la fréquence de vos entraînements et surveillez votre alimentation."

        # Ajouter des détails dans la réponse
        return Response({
            "advice": advice,
            "bmi": bmi,
            "performance_score": performance_score,
            "total_sessions": total_sessions,
            "avg_performance_notes": avg_performance_notes,
        })

