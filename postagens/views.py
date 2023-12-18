from django.views import generic
from .models import Postagem
from .forms import PostagemForm
from django.urls import reverse_lazy


class PostagemCreateView(generic.CreateView):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy('core:inicio')


class PostagemUpdateView(generic.UpdateView):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy('core:inicio')


class PostagemDeleteView(generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy('core:inicio')
