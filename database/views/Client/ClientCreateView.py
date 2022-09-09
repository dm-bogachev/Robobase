from database.forms.Client import ClientCreateForm
from database.models.Client import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class ClientCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Client
    template_name = 'database/Client/create.html'
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse_lazy('client_list')

    def model_name(self):
        return self.model._meta.verbose_name
