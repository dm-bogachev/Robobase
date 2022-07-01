from database.forms.Location import LocationCreateForm
from database.models.Location import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class LocationCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Location
    template_name = 'database/Location/create.html'
    form_class = LocationCreateForm

    def get_success_url(self):
        return reverse_lazy('location_list')

    def model_name(self):
        return self.model._meta.verbose_name
