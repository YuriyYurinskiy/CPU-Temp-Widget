import sensors
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
        text = ''
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                text += '%s at %s' % (chip, chip.adapter_name)
                for feature in chip:
                    text += '  %s: %.2f' % (feature.label, feature.get_value())
        finally:
            sensors.cleanup()

        return text
