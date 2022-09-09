from database.forms.Integrator import IntegratorCreateForm
from database.models.Integrator import Integrator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse


class IntegratorCreatePopup(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Integrator
    template_name = 'database/Integrator/create.html'
    form_class = IntegratorCreateForm

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_integrator");</script>' % (instance.pk, instance))

    def model_name(self):
        return self.model._meta.verbose_name