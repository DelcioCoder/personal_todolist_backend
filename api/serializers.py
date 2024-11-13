from rest_framework import serializers
from .models import Activity, Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'text', 'date_added']

class ActivitySerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True) # read only evita alterações diretas através do serializer

    class Meta:
        model = Activity
        fields = ['id', 'name', 'finished', 'date_added', 'day', 'notes']
