from django.forms import *
from database.models import Location


class LocationCreateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (LocationCreateForm, self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = Location
        fields = '__all__'
        exclude = ('deleted',)