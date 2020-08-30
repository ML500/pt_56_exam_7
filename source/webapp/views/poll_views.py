from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    paginate_by = 5
    context_object_name = 'polls'


class PollAddView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/add.html'
    success_url = reverse_lazy('index')
