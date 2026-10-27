
from rest_framework import serializers
from .models import DailyRecord


class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = [
            'id',
            'child_age',
            'food',
            'protein_foods',
            'sleep_hours',
            'outdoor_minutes',
            'study_minutes',
            'screen_minutes',
            'record_date',
            'ai_response',
        ]
        read_only_fields = ['id']
