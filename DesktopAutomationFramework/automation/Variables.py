from datetime import datetime as _td

from ..framework.Decorators.AutomationDecorator import AutomationHook

class _t:
    @AutomationHook
    @property
    def year(self):
        return _td.now().year

    @AutomationHook
    @property
    def month(self):
        return _td.now().month

    @AutomationHook
    @property
    def day(self):
        return _td.now().day

    @AutomationHook
    @property
    def hour(self):
        return _td.now().hour

    @AutomationHook
    @property
    def minute(self):
        return _td.now().minute

    @AutomationHook
    @property
    def second(self):
        return _td.now().second

    @AutomationHook
    def strftime(self, format_str):
        """ 
        %d day    (ex: 02)
        %m month  (ex: 04)
        %Y year   (ex: 2023)
        %y year   (ex: 23)
        %H hour   (ex: 12)
        %M minute (ex: 60)
        %S second (ex: 45)
        """
        return _td.now().strftime(format_str)
    
class vars:
    time = _t()