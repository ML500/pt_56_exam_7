from django.views.generic import ListView

from webapp.models import Poll


class IndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    paginate_by = 5
    context_object_name = 'polls'
