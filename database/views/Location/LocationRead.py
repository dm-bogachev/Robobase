from database.models.Location import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class LocationRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Location

    def model_name(self):
        return self.model._meta.verbose_name
