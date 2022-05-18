from rest_framework import serializers
from .models import NewUserDetails


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUserDetails
        fields = ('name', 'score')