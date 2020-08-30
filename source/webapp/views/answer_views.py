from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from webapp.models import Poll, Choice, Answer
from webapp.forms import AnswerForm


# class AnswerCreateView(TemplateView):
#     template_name = 'answers/create.html'
# 
#     def dispatch(self, request, *args, **kwargs):
#         self.poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
#         return super().dispatch(request, *args, **kwargs)
# 
#     def get_context_data(self, **kwargs):
#         kwargs['poll'] = self.poll
#         return super().get_context_data(**kwargs)
# 
#     def post(self, request, *args, **kwargs):
#         choice = get_object_or_404(Choice, pk=request.POST.get('choice', 0))
#         self.poll.answers.create(choice=choice)
#         return redirect(self.poll.get_absolute_url())


class AnswerCreateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answers/create.html'

    def dispatch(self, request, *args, **kwargs):
        self.poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['poll'] = self.poll
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.poll = self.poll
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['poll_choices'] = self.poll.choices.all()
        return kwargs

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})
