from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Poll, Choice
from webapp.forms import ChoiceForm


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choices/create.html'

    def dispatch(self, request, *args, **kwargs):
        self.poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['poll'] = self.poll
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.poll = self.poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})


class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choices/update.html'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choices/delete.html'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})
