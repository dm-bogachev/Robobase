from database.models.Client import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class ClientList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Client
    template_name = 'database/Client/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Client.objects.exclude(deleted=True)
        return qs

    def model_name(self):
        return self.model._meta.verbose_name
