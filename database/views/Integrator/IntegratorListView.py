from database.models.Integrator import Integrator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class IntegratorList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Integrator
    template_name = 'database/Integrator/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Integrator.objects.exclude(deleted=True)
        return qs

    def model_name(self):
        return self.model._meta.verbose_name
