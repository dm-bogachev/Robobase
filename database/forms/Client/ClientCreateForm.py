from django.forms import *
from database.models import Client


class ClientCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (ClientCreateForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('deleted',)