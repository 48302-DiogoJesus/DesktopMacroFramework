import time
import pygetwindow as gw

from framework.Decorators.AutomationDecorator import AutomationHook

WindowNotFoundError = Exception("Window not found")

@AutomationHook
def wait(partial_title: str, timeout_s: int = 2):
    time_passed_s = 0

    actual_window_title = ""
    while True:
        try:
            actual_window_title = str(gw.getActiveWindowTitle()).lower()
        except: 
            pass

        is_in_expected_window = actual_window_title.find(partial_title.lower()) != -1
        if is_in_expected_window:
            return
        
        time.sleep(0.1) # 100 ms
        time_passed_s += 0.1

        if time_passed_s > timeout_s:
            raise WindowNotFoundError
        else:
            continue

@AutomationHook
def select(partial_title: str):
    windows = gw.getWindowsWithTitle(partial_title)

    if windows:
        # If there are multiple windows with the partial title, choose the first one
        window = windows[0]
        window.activate()
        return True
    else:
        return False