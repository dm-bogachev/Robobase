import imp
from django.urls import path

from django.views.generic import TemplateView
class TestView(TemplateView):
    template_name = 'test.html'

urlpatterns = [
    path('', TestView.as_view(), name='home')
]