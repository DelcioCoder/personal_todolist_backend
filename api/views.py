from django.shortcuts import render
from rest_framework import generics
from todolist.models import Activity, Note, Modality
from rest_framework.permissions import IsAuthenticated
from .serializers import ActivitySerializer, NoteSerializer

# Lista de atividades e criação de nova atividade
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado

    def perform_create(self, serializer):
        # Recupera o ID da modalidade enviado na requisição
        modality_id = self.request.data.get('modality_id')
        
        # Verifica se a modalidade existe
        modality = Modality.objects.get(id=modality_id)
        
        # Cria a atividade associada à modalidade
        serializer.save(modality=modality)

# Exibe, atualiza ou deleta uma atividade específica
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado

# Lista de notas e criação de nova nota
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado

    def perform_create(self, serializer):
        # Obtém o ID da atividade associada à nota
        activity_id = self.request.data.get('activity')
        
        # Verifica se a atividade existe
        activity = Activity.objects.get(id=activity_id)
        
        # Cria a nota associada à atividade
        serializer.save(activity=activity)

# Exibe, atualiza ou deleta uma nota específica
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado
