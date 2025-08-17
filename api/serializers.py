from rest_framework import serializers
from todolist.models import Activity, Note, Modality

class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ['id', 'name', 'description']

class NoteSerializer(serializers.ModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'text', 'date_added', 'activity']

class ActivitySerializer(serializers.ModelSerializer):
    modality = ModalitySerializer(read_only=True)  # Somente leitura
    modality_id = serializers.PrimaryKeyRelatedField(queryset=Modality.objects.all(), source='modality',  write_only=True)
    notes = NoteSerializer(many=True, read_only=True) # read only evita alterações diretas através do serializer

    class Meta:
        model = Activity
        fields = ['id', 'finished', 'date_added', 'day', 'modality', 'modality_id', 'notes']
