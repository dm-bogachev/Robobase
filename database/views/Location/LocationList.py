from database.models.Location import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class LocationList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Location

    def model_name(self):
        return self.model._meta.verbose_name
