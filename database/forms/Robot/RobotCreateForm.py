from django.forms import *

from database.models import Integrator, Location, Robot
from database.models.Client import Client
from database.models.RobotArm import RobotArm
from database.models.RobotController import RobotController

class RobotCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (RobotCreateForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['controller'].queryset = RobotController.objects.filter(deleted=False)
        self.fields['arm'].queryset = RobotArm.objects.filter(deleted=False)
        self.fields['client'].queryset = Client.objects.filter(deleted=False)
        self.fields['integrator'].queryset = Integrator.objects.filter(deleted=False)
        self.fields['location'].queryset = Location.objects.filter(deleted=False)
    class Meta:
        model = Robot
        fields = '__all__'
        exclude = ('added_by','deleted',)