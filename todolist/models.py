from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


class Activity(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    #Mantém o dia máximo de 30 dias para cada actividade individual
    day = models.IntegerField(validators=[MaxValueValidator(30)], help_text="Dia 1 de 30 para o desafio de 30 dias.")


    def clean(self):

        # Limita o número de dias a no máximo 30 dias, aplicado globalmente ao desafio

        if Activity.objects.filter(day__lte=30).count() >= 30: #O sufixo lte vem de less than or equal, ou seja, menor ou igual.
            raise ValidationError("O número total de dias não pode exceder 30 dias para o desadio.") 
        

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'Activities'


class Note(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.name} - Nota do dia {self.activity.day}: {self.text[:50]}..."
    
    class Meta:
        ordering =  ['date_added']