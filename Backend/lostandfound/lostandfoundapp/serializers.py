from rest_framework import serializers

from .models import LostAndFound


class LostAndFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostAndFound
        fields = '__all__'