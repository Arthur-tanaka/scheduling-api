from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone=validated_data.get('phone', ''),
            password=validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'password']
        