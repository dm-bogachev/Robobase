from database.forms.RobotService import RobotServiceForm
from database.models import RobotService
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotServiceCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotService
    template_name = 'database/RobotService/create.html'
    form_class = RobotServiceForm
    # fields = ['date', 'description']

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        form.instance.robot = robot
        form.save()
        return super(RobotServiceCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name
