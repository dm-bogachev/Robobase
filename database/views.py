from django.urls import reverse_lazy
from django.views.generic import *
from .models import *

class RobotDetail(DetailView):
    model = Robot

class RobotList(ListView):
    model = Robot

class RobotCreate(CreateView):
    model = Robot
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robot_list')
