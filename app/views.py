
from django.views import generic
from .models import Comentario,Ticket,Categoria
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_ticket_list'

    def get_queryset(self):
        """Return the last 15 published tickets."""
       # return Question.objects.order_by('-pub_date')[:15]
        return Ticket.objects.filter(
                fechaT__lte=timezone.now()    #PAara que no haya tickets cuya fecha de publicacion es futura
            ).order_by('-fechaT')#[:15]



class TicketView(generic.DetailView):
    model = Ticket
    template_name = 'app/ticket.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Ticket.objects.filter(fechaT__lte=timezone.now())




