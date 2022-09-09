from database.forms.Location import LocationCreateForm
from database.models.Location import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse


class LocationCreatePopup(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Location
    template_name = 'database/Location/create.html'
    form_class = LocationCreateForm

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_location");</script>' % (instance.pk, instance))

    def model_name(self):
        return self.model._meta.verbose_name