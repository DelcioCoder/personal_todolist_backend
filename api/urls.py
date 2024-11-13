from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView, NoteListCreateView, NoteDetailView


urlpatterns = [
    # Endpoints para atividades
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),



    # Endpoints para notas
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]
