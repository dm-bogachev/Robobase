from database.models import RobotController
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotControllerCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotController
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robotcontroller_list')

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
        return super(RobotControllerCreate, self).form_valid(form)
