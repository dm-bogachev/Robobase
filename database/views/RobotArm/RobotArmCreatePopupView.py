from database.forms.RobotArm import RobotArmCreateForm
from database.models.RobotArm import RobotArm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse


class RobotArmCreatePopup(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/RobotArm/create.html'
    form_class = RobotArmCreateForm

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_robotarm");</script>' % (instance.pk, instance))

    def model_name(self):
        return self.model._meta.verbose_name