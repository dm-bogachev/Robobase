from django.urls import path
from .views import *


from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'test.html'


urlpatterns = [
    path('', RedirectView.as_view(url='robot/list'), name='home'),
    #path('', TestView.as_view(), name='home'),
    # Robot
    path('robot/list', RobotList.as_view(), name='robot_list'),
    path('robot/create', RobotCreate.as_view(), name='robot_create'),
    path('robot/read/<int:pk>', RobotRead.as_view(), name='robot_read'),
    path('robot/update/<int:pk>', RobotUpdate.as_view(), name='robot_update'),
    path('robot/delete/<int:pk>', RobotDelete.as_view(), name='robot_delete'),
    # Location
    path('location/create', LocationCreate.as_view(), name='location_create'),
    path('location/read/<int:pk>', LocationRead.as_view(), name='location_read'),
    path('location/update/<int:pk>',
         LocationUpdate.as_view(), name='location_update'),
    path('location/delete/<int:pk>',
         LocationDelete.as_view(), name='location_delete'),
    path('location/list', LocationList.as_view(), name='location_list'),
    # Client
    path('client/create', ClientCreate.as_view(), name='client_create'),
    path('client/read/<int:pk>', ClientRead.as_view(), name='client_read'),
    path('client/update/<int:pk>', ClientUpdate.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDelete.as_view(), name='client_delete'),
    path('client/list', ClientList.as_view(), name='client_list'),
    # Integrator
    path('integrator/create', IntegratorCreate.as_view(), name='integrator_create'),
    path('integrator/read/<int:pk>',
         IntegratorRead.as_view(), name='integrator_read'),
    path('integrator/update/<int:pk>',
         IntegratorUpdate.as_view(), name='integrator_update'),
    path('integrator/delete/<int:pk>',
         IntegratorDelete.as_view(), name='integrator_delete'),
    path('integrator/list', IntegratorList.as_view(), name='integrator_list'),
    # RobotArm
    path('robotarm/create', RobotArmCreate.as_view(), name='robotarm_create'),
    path('robotarm/read/<int:pk>', RobotArmRead.as_view(), name='robotarm_read'),
    path('robotarm/update/<int:pk>',
         RobotArmUpdate.as_view(), name='robotarm_update'),
    path('robotarm/delete/<int:pk>',
         RobotArmDelete.as_view(), name='robotarm_delete'),
    path('robotarm/list', RobotArmList.as_view(), name='robotarm_list'),
    # RobotController
    path('robotcontroller/create', RobotControllerCreate.as_view(),
         name='robotcontroller_create'),
    path('robotcontroller/read/<int:pk>',
         RobotControllerRead.as_view(), name='robotcontroller_read'),
    path('robotcontroller/update/<int:pk>',
         RobotControllerUpdate.as_view(), name='robotcontroller_update'),
    path('robotcontroller/delete/<int:pk>',
         RobotControllerDelete.as_view(), name='robotcontroller_delete'),
    path('robotcontroller/list', RobotControllerList.as_view(),
         name='robotcontroller_list'),
    # RobotFile
    path('robotfile/create/<int:pk>', RobotFileCreate.as_view(),
         name='robotfile_create'),
    path('robotfile/delete/<int:pk>', RobotFileDelete.as_view(),
         name='robotfile_delete'),
    # RobotService
    path('robotservice/create/<int:pk>', RobotServiceCreate.as_view(),
         name='robotservice_create'),
    path('robotservice/delete/<int:pk>', RobotServiceDelete.as_view(),
         name='robotservice_delete'),
]
