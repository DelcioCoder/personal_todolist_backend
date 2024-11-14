from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator



class Modality(models.Model):
    # Modalidade do desafio, ex: "Exercício Físico", "Leitura"
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Modalities'

class Activity(models.Model):
    finished = models.BooleanField(default=False)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE, related_name='activities')
    date_added = models.DateTimeField(auto_now_add=True)

    #Mantém o dia máximo de 30 dias para cada actividade individual
    day = models.IntegerField(validators=[MaxValueValidator(30)], help_text="Dia 1 de 30 para o desafio de 30 dias.")


    def clean(self):

        # Limita o número de dias de actividades por modalidade  a no máximo 30 dias, aplicado globalmente ao desafio

        if Activity.objects.filter(day__lte=30, modality=self.modality).count() >= 30: #O sufixo lte vem de less than or equal, ou seja, menor ou igual.
            raise ValidationError("O número total de dias não pode exceder 30 dias para o desadio.") 
        

    def __str__(self):
        return f'{self.modality.name} - Dia {self.day}'
    
    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'Activities'


class Note(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.modality.name} - Nota do dia {self.activity.day}: {self.text[:50]}..."
    
    class Meta:
        ordering =  ['date_added']