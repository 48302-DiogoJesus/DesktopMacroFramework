import time
from pynput.keyboard import Key, Controller
import keyboard
from framework.Decorators.AutomationDecorator import AutomationHook

keyboard = Controller()

@AutomationHook
def write(text: str):
    keyboard.type(text)

@AutomationHook
def keys(*args: Key | str, repeat_times: int = 1, repeat_interval_s: float = 0.3):
    keys = [item.lower() if isinstance(item, str) else item for item in args]

    for _ in range(repeat_times):
        # Press all keys
        for key in keys:
            keyboard.press(key)
        
        # Release all keys
        for key in keys:
            try:
                if keyboard.pressed(key): keyboard.release(key)
            except: pass

        # Only wait if there will be a second iteration
        if repeat_times > 1:
            time.sleep(repeat_interval_s)
