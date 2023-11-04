import time
from pynput.keyboard import Key, Controller

from ..framework.Decorators.AutomationDecorator import AutomationHook

kboard = Controller()

class keyboard:
    @AutomationHook
    @staticmethod
    def write(text: str):
        kboard.type(text)

    @AutomationHook
    @staticmethod
    def keys(*args: Key | str, repeat_times: int = 1, repeat_interval_s: float = 0.3):
        keys = [item.lower() if isinstance(item, str) else item for item in args]

        for _ in range(repeat_times):
            # Press all keys
            for key in keys:
                kboard.press(key)
            
            # Release all keys
            for key in keys:
                try:
                    if kboard.pressed(key): kboard.release(key)
                except: pass

            # Only wait if there will be a second iteration
            if repeat_times > 1:
                time.sleep(repeat_interval_s)
