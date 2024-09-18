from user.models.custom_user_model import CustomUserModel
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'weight', 'size',
                  'age', 'numbers']
