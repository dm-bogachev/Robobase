from database.models import RobotFile
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotFileCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotFile
    template_name = 'database/RobotFile/create.html'
    fields = ['display_name', 'file', 'type', 'service']

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        form.instance.robot = robot
        form.save()
        return super(RobotFileCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name
