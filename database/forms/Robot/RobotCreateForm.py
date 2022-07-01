from django.forms import *

from database.models import Robot

class RobotCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (RobotCreateForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = Robot
        fields = '__all__'
        exclude = ('added_by',)