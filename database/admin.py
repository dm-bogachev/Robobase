from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

admin.site.register(Location, SimpleHistoryAdmin)
admin.site.register(Client, SimpleHistoryAdmin)
admin.site.register(Integrator, SimpleHistoryAdmin)
admin.site.register(RobotArm, SimpleHistoryAdmin)
admin.site.register(RobotController, SimpleHistoryAdmin)
admin.site.register(Robot, SimpleHistoryAdmin)
admin.site.register(RobotFile, SimpleHistoryAdmin)
admin.site.register(RobotVendor, SimpleHistoryAdmin)
admin.site.register(RobotService, SimpleHistoryAdmin)
admin.site.register(RobotSeller, SimpleHistoryAdmin)

