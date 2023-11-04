import time
from framework.Decorators.AutomationDecorator import AutomationHook

@AutomationHook
def wait(seconds: int):
    time.sleep(seconds)

@AutomationHook
def end():
    exit()
