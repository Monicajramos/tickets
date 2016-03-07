from django.views import generic
from django.shortcuts import render, redirect
from .models import Comentario, Ticket, Categoria
from django.utils import timezone
from .forms import Formulario1,Formulario2


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_ticket_list'

    def get_queryset(self):
        """Return the last 15 published tickets."""
        # return Question.objects.order_by('-pub_date')[:15]
        return Ticket.objects.filter(
            fechaT__lte=timezone.now()  # PAara que no haya tickets cuya fecha de publicacion es futura
        ).order_by('-fechaT')  # [:15]


class TicketView(generic.DetailView):
    model = Ticket
    template_name = 'app/ticket.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Ticket.objects.filter(fechaT__lte=timezone.now())


def addTicket(request):
    if request.method == "POST":
        form = Formulario1(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # cogemos los datos del formulario pero NO guardamos el ticket(commuit=false)
            # ticket.author = request.user            asignamos al ticket el autor conectado
            # ticket.published_date = timezone.now()  asignamos al ticket la fecha de publicacion
            ticket.save()  # GUARDAMOS EL TICKET
            return redirect('app:index')
    else:
        form = Formulario1()
    return render(request, 'app/formularioT.html', {'form': form})

def addComment(request):
    if request.method == "POST":
        form = Formulario2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = Formulario2()
    return render(request, 'app/formularioT.html', {'form': form})
