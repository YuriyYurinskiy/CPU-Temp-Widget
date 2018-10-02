import os
from jadi import component

from aj.plugins.dashboard.api import Widget


@component(Widget)
class RandomWidget(Widget):
    id = 'cpu_temp'

    # display name
    name = 'CPU Temp'

    # template of the widget
    template = '/cpu_temp_widget:resources/partial/widget.html'

    def __init__(self, context):
        Widget.__init__(self, context)

    def get_value(self, config):
        if 'bytes' not in config:
            return 'Not configured'
        return os.urandom(int(config['bytes'])).encode('hex')
