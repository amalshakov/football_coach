from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm  # Из какого класса взять форму
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
