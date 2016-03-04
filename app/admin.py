from django.contrib import admin
from .models import Comentario,Ticket,Categoria
# Register your models here.

admin.site.register(Comentario)
admin.site.register(Ticket)
admin.site.register(Categoria)