from django.forms import *

from database.models import Robot
from database.models.RobotService import RobotService

class RobotServiceForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (RobotServiceForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = RobotService
        fields = '__all__'
        exclude = ('robot',)