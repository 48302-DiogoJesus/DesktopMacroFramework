import tkinter as tk
from typing import Any
from pymsgbox import alert as _alert, confirm as _confirm, prompt as _prompt, OK_TEXT as OK, YES_TEXT as YES, NO_TEXT as NO, CANCEL_TEXT as CANCEL, IGNORE_TEXT as IGNORE, CONTINUE_TEXT as CONTINUE, RETRY_TEXT as RETRY

from framework.Decorators.AutomationDecorator import AutomationHook

@AutomationHook
def alert(text: str, title: str = ""):
   return  _alert(text, title, _tkinter=False)

@AutomationHook
def confirm(text: str, title: str = "", buttons: Any = (OK, CANCEL)):
    return _confirm(text, title, buttons, _tkinter=False)

@AutomationHook
def prompt(text: str, title: str = "", default: str = ""):
    return _prompt(text, title, default)

@AutomationHook
def optionMenu(*options: str, stop_if_no_selection: bool = True):
    selected_option = None

    def on_select(option):
        nonlocal selected_option
        selected_option = option
        root.destroy()

    root = tk.Tk()
    root.title("Select an Option")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - root.winfo_reqwidth()) // 2
    y = (screen_height - root.winfo_reqheight()) // 2
    root.geometry(f"+{x}+{y}")

    for option in options:
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)
        button = tk.Button(frame, text=option, command=lambda o=option: on_select(o))
        button.pack(fill=tk.BOTH, expand=True)

    # root.protocol("WM_DELETE_WINDOW", root.quit)  # Handle window close button

    root.mainloop()

    if selected_option is None and stop_if_no_selection:
        raise Exception("No option selected")

    return selected_option