from database.models.Integrator import Integrator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class IntegratorRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Integrator
    template_name = 'database/Integrator/read.html'

    def model_name(self):
        return self.model._meta.verbose_name
