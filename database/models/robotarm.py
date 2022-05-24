import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords


class RobotArm(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        fname = [str(instance.name), str(randint(0, maxsize)), filename]
        return os.path.join('arm_images',
                            '_'.join(fname),)

    vendor = models.ForeignKey('RobotVendor',
                               on_delete=models.SET_DEFAULT,
                               verbose_name='Производитель',
                               default=1,)  # default = 'Kawasaki'

    name = models.CharField(max_length=32,
                            verbose_name='Модель',
                            db_index=True,)

    image = models.ImageField(upload_to=get_file_path,
                              verbose_name='Изображение',
                              null=True,
                              blank=True,)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
        return str(self.vendor) + '/' + self.name

    class Meta:
        verbose_name_plural = 'Модели'
        verbose_name = 'Модель'
        unique_together = ('vendor', 'name',)


class RobotArmCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robotarm_list')

    def model_name(self):
        return self.model._meta.verbose_name

    def dispatch(self, request, *args, **kwargs):
        self.image = request.FILES.pop('image', None)
        if isinstance(self.image, list) and len(self.image) > 0:
            self.image = self.image[0]
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        if self.image:
            upload_to = form.instance.image.field.upload_to(
                form.instance, self.image.name)
            save_folder = settings.MEDIA_ROOT + upload_to
            with open((save_folder), 'wb+') as f:
                for chunk in self.image.chunks():
                    f.write(chunk)
            form.instance.image = upload_to
        return super(RobotArmCreate, self).form_valid(form)


class RobotArmRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = RobotArm

    def model_name(self):
        return self.model._meta.verbose_name


class RobotArmUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robotarm_list')

    def model_name(self):
        return self.model._meta.verbose_name

    def dispatch(self, request, *args, **kwargs):
        self.image = request.FILES.pop('image', None)
        if isinstance(self.image, list) and len(self.image) > 0:
            self.image = self.image[0]
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        if self.image:
            upload_to = form.instance.image.field.upload_to(
                form.instance, self.image.name)
            save_folder = settings.MEDIA_ROOT + upload_to
            with open((save_folder), 'wb+') as f:
                for chunk in self.image.chunks():
                    f.write(chunk)
            form.instance.image = upload_to
        return super(RobotArmUpdate, self).form_valid(form)


class RobotArmDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        return reverse_lazy('robotarm_list')

    def model_name(self):
        return self.model._meta.verbose_name


class RobotArmList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = RobotArm

    def model_name(self):
        return self.model._meta.verbose_name
