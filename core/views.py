from django.views import generic
from postagens.models import Postagem



class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postagens'] = Postagem.objects.all()
        return context
