from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    status = serializers.CharField(required=False, allow_blank=True, max_length=30)
    status = serializers.CharField(required=False, allow_blank=True, max_length=1000)