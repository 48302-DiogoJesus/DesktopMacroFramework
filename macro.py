from DesktopAutomationFramework import keyboard, windows, input, vars, Macro, wait, end

""" 
TODO
- DONE fix window.select
- DONE Key comes by importing keyboard
    - LATER Simplify key selection
- Add characters as Keys ?
- + check other modules
- try to hide irrelevant imports
"""

@Macro(interval_s=1)
def macro():
    keyboard.keys(keyboard.key.win)
    keyboard.write("notepad++")
    keyboard.keys(keyboard.key.enter)
    windows.wait("notepad++", 2)
    
    windows.select("macroframe")


macro()
