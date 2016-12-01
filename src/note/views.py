from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from note.models import Note, NoteFilter
from note.forms import NoteForm
from member.models import Client


# Create your views here.

class NoteList(generic.ListView):
    # Display the list of notes
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        uf = NoteFilter(self.request.GET)
        return uf.qs

        # The queryset must be client

    def get_context_data(self, **kwargs):
        uf = NoteFilter(self.request.GET, queryset=self.get_queryset())

        context = super(NoteList, self).get_context_data(**kwargs)

        # Here you add some variable of context to display on template
        context['filter'] = uf
        return context


class ClientNoteList(LoginRequiredMixin, generic.ListView):
    # Display detail of one client
    model = Note
    template_name = 'notes_client_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = NoteFilter(
            self.request.GET,
            queryset=Note.objects.filter(
                client__id=self.kwargs['pk'])).qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ClientNoteList, self).get_context_data(**kwargs)
        context['active_tab'] = 'notes'
        context['client_status'] = Client.CLIENT_STATUS
        context['client'] = get_object_or_404(Client, id=self.kwargs['pk'])
        context['filter'] = NoteFilter(
            self.request.GET, queryset=Note.objects.filter(
                client__id=self.kwargs['pk']))

        return context


@login_required
def NoteAdd(request):
    pass


@login_required
def mark_as_read(request, id):
    note = get_object_or_404(Note, pk=id)
    note.mark_as_read()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def mark_as_unread(request, id):
    note = get_object_or_404(Note, pk=id)
    note.mark_as_unread()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
