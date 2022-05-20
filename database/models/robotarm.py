from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse_lazy
from django.views.generic import *
import os


class RobotArm(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        fname = [str(instance.name), str(randint(0, maxsize)), filename]
        return os.path.join('arm_images',
                            '_'.join(fname),)

    name = models.CharField(max_length=32,
                            unique=True,
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
        return self.name

    class Meta:
        verbose_name_plural = 'Модели'
        verbose_name = 'Модель'


class RobotArmCreate(CreateView):
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


class RobotArmRead(DetailView):
    model = RobotArm

    def model_name(self):
        return self.model._meta.verbose_name


class RobotArmUpdate(UpdateView):
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


class RobotArmDelete(DeleteView):
    model = RobotArm
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        return reverse_lazy('robotarm_list')

    def model_name(self):
        return self.model._meta.verbose_name


class RobotArmList(ListView):
    model = RobotArm

    def model_name(self):
        return self.model._meta.verbose_name
