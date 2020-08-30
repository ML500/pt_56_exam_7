from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.models import Poll, Choice


class AnswerCreateView(TemplateView):
    template_name = 'answers/create.html'

    def dispatch(self, request, *args, **kwargs):
        self.poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['poll'] = self.poll
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        choice = get_object_or_404(Choice, pk=request.POST.get('choice', 0))
        self.poll.answers.create(choice=choice)
        return redirect(self.poll.get_absolute_url())
