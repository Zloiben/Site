from django.db.models import Count

from .models import *


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('post'))
        context['cats'] = cats
        context['auth'] = self.request.user.is_authenticated
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

    @staticmethod
    def join_context(*args: dict):
        result = []
        for context in args:
            result.extend(list(context.items()))
        return dict(result)
