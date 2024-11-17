from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView, NoteListCreateView, NoteDetailView

urlpatterns = [
    # Endpoints para atividades
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),

    # Endpoints para notas relacionadas à atividade
    path('activities/<int:activity_id>/notes/', NoteListCreateView.as_view(), name='note-list-create'),  # Adicione activity_id aqui
    path('activities/<int:activity_id>/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),  # Id para cada nota
]
