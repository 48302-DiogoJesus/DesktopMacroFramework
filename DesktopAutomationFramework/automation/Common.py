import time

from ..framework.Variables import RWVariables
from ..framework.Decorators.MacroDecorator import Macro
from ..framework.Decorators.AutomationDecorator import AutomationDecorator

@AutomationDecorator
def wait(seconds: int):
    time.sleep(seconds)

# Ends the CURRENT macro execution! (by killing its Thread). Doesn't end the GUI.
@AutomationDecorator
def end():
    exit()

@AutomationDecorator
def pause():
    Macro.onMacroPause()