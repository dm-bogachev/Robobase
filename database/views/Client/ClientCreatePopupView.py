from database.forms.Client import ClientCreateForm
from database.models.Client import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse


class ClientCreatePopup(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Client
    template_name = 'database/Client/create.html'
    form_class = ClientCreateForm()

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_client");</script>' % (instance.pk, instance))

    def model_name(self):
        return self.model._meta.verbose_name
