from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('name', 'score')

class GetScoreSerializer(serializers.Serializer):
    rank = serializers.IntegerField()