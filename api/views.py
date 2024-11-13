from django.shortcuts import render
from rest_framework import generics
from todolist.models import Activity, Note
from .serializers import ActivitySerializer, NoteSerializer
# Create your views here.



# Lista de atividades e criação de nova atividade
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


#Exibe, actualiza ou deleta uma actividade específica
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer



#Lista de notas e criação de nova nota
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


#Exibe, actualiza ou deleta uma nota específica
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer