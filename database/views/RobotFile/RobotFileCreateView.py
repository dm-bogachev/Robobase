from database.models import RobotFile
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from database.models.RobotSeller import RobotSeller
from database.models.RobotService import RobotService


class RobotFileCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotFile
    template_name = 'database/RobotFile/create.html'
    fields = ['file', 'display_name', 'service']

    TYPES = {
        'photo': ['png', 'jpg', 'jpeg'],
        'video': ['avi', 'mp4', 'webm'],
        'backup': ['pg', 'as', 'el', 'ol'],
        'docs': ['pdf', 'docx', 'doc', 'xls'],
    }

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        # Auto type set
        type_set = False
        import os.path
        extension = os.path.splitext(form.instance.file.path)[1][1:]
        for key in self.TYPES:
            if (extension in self.TYPES[key]):
                form.instance.type = key
                type_set = True
        if not type_set: form.instance.type = 'other'
        if form.instance.display_name == '':
            form.instance.display_name = form.instance.file.name
        form.instance.robot = robot
        form.save()
        return super(RobotFileCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        services = RobotService.objects.filter(robot=robot)
        context['form'].fields['service'].queryset = services
        #
        return context

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name


        # ('photo', 'Фото'),
        # ('video', 'Видео'),
        # ('backup', 'Резервная копия'),
        # ('report', 'Oтчет по работам'),
        # ('check', 'Чек-лист'),
        # ('other', 'Другое'),
        # ('docs', 'Документы'),)