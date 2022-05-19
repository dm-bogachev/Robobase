from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Integrator)
admin.site.register(RobotArm)
admin.site.register(RobotController)
admin.site.register(Robot)
admin.site.register(RobotFile)