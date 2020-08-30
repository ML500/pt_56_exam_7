from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    paginate_by = 5
    context_object_name = 'polls'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/create.html'


class PollUpdateView(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/update.html'


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'polls/delete.html'
    success_url = reverse_lazy('index')
