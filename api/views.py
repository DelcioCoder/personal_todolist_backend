from django.shortcuts import render
from rest_framework import generics
from todolist.models import Activity, Note
from rest_framework.permissions import IsAuthenticated
from .serializers import ActivitySerializer, NoteSerializer
# Create your views here.



# Lista de atividades e criação de nova atividade
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated] # Garante que o usuário está autenticado


#Exibe, actualiza ou deleta uma actividade específica
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated] # Garante que o usuário está autenticado



#Lista de notas e criação de nova nota
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Garante que o usuário está autenticado


#Exibe, actualiza ou deleta uma nota específica
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Garante que o usuário está autenticado