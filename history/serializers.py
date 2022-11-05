from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = "history.History"
        fields = "__all__"


class CreateSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    sort = serializers.CharField(max_length=1)
    comment = serializers.CharField()
