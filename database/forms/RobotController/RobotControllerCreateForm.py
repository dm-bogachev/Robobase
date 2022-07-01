from django.forms import *

from database.models import Integrator, Location, Robot
from database.models.Client import Client
from database.models.RobotArm import RobotArm
from database.models.RobotController import RobotController

class RobotControllerCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (RobotControllerCreateForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = RobotController
        fields = '__all__'
        exclude = ('deleted',)