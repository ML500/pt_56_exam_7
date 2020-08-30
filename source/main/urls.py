"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.models import Poll
from webapp import views


def make_crud_patterns(model, views_module, is_index=False, actions=None, prefix=''):
    patterns = []
    path_templates = {
        'list': '{}s/list/',
        'detail': '{}/<int:pk>/',
        'create': '{}s/create/',
        'update': '{}/<int:pk>/update/',
        'delete': '{}/<int:pk>/delete/',
    }
    if not actions:
        actions = ['list', 'detail', 'create', 'update', 'delete']
    if is_index and 'list' in actions:
        patterns.append(path('', getattr(views_module, 'IndexView').as_view(), name='index'))
        actions.remove('list')
    model_name = model.__name__
    model_name_lower = model_name.lower()
    for action in actions:
        view = getattr(views_module, model_name + action.capitalize() + 'View').as_view()
        new_path = path_templates[action].format(model_name_lower)
        if prefix:
            new_path = prefix + '/' + new_path
        path_name = model_name_lower + '_' + action
        patterns.append(path(new_path, view, name=path_name))
    return patterns


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += make_crud_patterns(Poll, views, is_index=True)
