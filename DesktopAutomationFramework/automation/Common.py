import time

from ..framework.Decorators.MacroDecorator import Macro
from ..framework.Decorators.AutomationDecorator import AutomationDecorator

@AutomationDecorator
def wait(seconds: int):
    time.sleep(seconds)

@AutomationDecorator
def end():
    exit()

@AutomationDecorator
def pause():
    Macro.onMacroPause()