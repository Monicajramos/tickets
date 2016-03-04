from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.


class Categoria(models.Model):
    categoria=models.CharField(max_length=100)
    def __str__(self):
        return self.categoria


class Ticket(models.Model):
    categoriaT = models.ForeignKey(Categoria)  #relacion 1Ticket-1Categoria
    tituloT = models.CharField(max_length=100)
    descripcionT = models.CharField(max_length=350)
    fechaT = models.DateTimeField('fecha ticket')
    autorT =  models.ForeignKey(User , related_name="autor Ticket+")                 #porq estamos usando una clase propia django
    responsableT = models.ForeignKey(User, related_name="responsable Ticket+")
    def __str__(self):
        return self.tituloT
    def was_published_recently(self):
        return self.fechaT >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'fechaT'

class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket)  #relacion 1Comentario-1Ticket
    descripcionC = models.CharField(max_length=350)
    fechaC = models.DateTimeField('fecha comentario')
    autorC =  models.ForeignKey(User)
    def __str__(self):
        return self.descripcionC
