from database.models.Client import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class ClientRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Client

    template_name = 'database/Client/read.html'

    def model_name(self):
        return self.model._meta.verbose_name
