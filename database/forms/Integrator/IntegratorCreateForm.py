from django.forms import *
from database.models import Client, Integrator


class IntegratorCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (IntegratorCreateForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = Integrator
        fields = '__all__'
        exclude = ('deleted',)