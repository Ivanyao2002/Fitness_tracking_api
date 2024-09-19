from rest_framework import viewsets
from user.models.custom_user_model import CustomUserModel
from api.serializers.custom_user_serializer import CustomUserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password



class CustomerUserViewSet(viewsets.ModelViewSet):

    serializer_class = CustomUserSerializer
    queryset = CustomUserModel.objects.all()

    @action(detail=False, methods=['post'])
    def create_user_with_crypt(self, request,pk=None):
        data=JSONParser().parse(request)
        serializer= CustomUserSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save(password=make_password(data['password']))

            return JsonResponse({'statut':'OK'}, status=204)
        
        return JsonResponse(serializer.erros, status=400)
