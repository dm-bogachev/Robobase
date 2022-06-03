from database.models.Integrator import Integrator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class IntegratorUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Integrator
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('integrator_list')

    def model_name(self):
        return self.model._meta.verbose_name
