from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Modality, Activity

class ActivityModelTest(TestCase):
    def setUp(self):
        self.modality = Modality.objects.create(name="Leitura")

    def test_activity_limit_per_modality(self):
        # Cria 30 atividades para a mesma modalidade
        for i in range(30):
            Activity.objects.create(modality=self.modality, day=i + 1)

        # Tenta criar a 31ª atividade
        with self.assertRaises(ValidationError):
            activity = Activity(modality=self.modality, day=31)
            activity.full_clean()  # full_clean() é necessário para rodar a validação do model

    def test_activity_creation_within_limit(self):
        # Tenta criar uma atividade dentro do limite
        try:
            activity = Activity(modality=self.modality, day=1)
            activity.full_clean()
        except ValidationError:
            self.fail("A criação da atividade falhou inesperadamente.")