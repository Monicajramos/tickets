from django import forms
from .models import Ticket,Comentario


class Formulario1(forms.ModelForm):

    class Meta:
        model = Ticket
        exclude = ["responsableT", "fechaT"]#porque al añadir un ticket no podemos elegir el responsable
                                 #si queremos poder elegir todos os campos ponemos exclude=[]


class Formulario2(forms.ModelForm):

    class Meta:
        model= Comentario
        exclude=["fechaT"]
