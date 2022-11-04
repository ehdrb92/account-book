from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = "history.History"
        fields = "__all__"
