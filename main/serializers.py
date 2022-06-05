from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'userId', 'loggedin')




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('userId', 'username', 'email', 'password')

    def create(self, validated_date):
        user = UserProfile.objects.create_user(
            validated_date["username"],
            validated_date["email"],
            validated_date["password"]
        )
        return user