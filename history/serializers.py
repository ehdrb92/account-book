from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["amount", "sort", "comment"]


class CreateSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    sort = serializers.CharField(max_length=1)
    comment = serializers.CharField()
