from django.db import models

# Create your models here.

class Agenda(models.Model):
    data = models.CharField(max_length=10)
    servico = models.CharField(max_length=500)
    
    def __str__(self):
        return "Data: "+self.data+" | Serviço(s): ["+ self.servico+"]"      