from database.forms.RobotController import RobotControllerCreateForm
from database.models.RobotController import RobotController
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse


class RobotControllerCreatePopup(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotController
    template_name = 'database/RobotController/create.html'
    form_class = RobotControllerCreateForm

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_robotcontroller");</script>' % (instance.pk, instance))

    def model_name(self):
        return self.model._meta.verbose_name