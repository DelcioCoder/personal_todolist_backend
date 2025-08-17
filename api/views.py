from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound, APIException
from todolist.models import Activity, Note, Modality
from rest_framework.permissions import IsAuthenticated
from .serializers import ActivitySerializer, NoteSerializer

# Lista de atividades e criação de nova atividade
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]


# Exibe, atualiza ou deleta uma atividade específica
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado

# Lista de notas e criação de nova nota
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obter o activity_id da URL
        activity_id = self.kwargs['activity_id']
        return Note.objects.filter(activity_id=activity_id)

    def perform_create(self, serializer):
        # Obtém o activity_id da URL
        activity_id = self.kwargs['activity_id']

        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            raise NotFound("Atividade não encontrada.")
        except Exception as e:
            raise APIException(f"Ocorreu um erro inesperado: {e}")

        # Cria a nota associada à atividade
        serializer.save(activity=activity)


# Exibe, atualiza ou deleta uma nota específica
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Garante que o usuário está autenticado
