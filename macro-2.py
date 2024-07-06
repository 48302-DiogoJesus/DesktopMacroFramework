from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end, pause

@Macro()
def macro():
    
    keyboard.keys(key.win)
    keyboard.write("https://outlook.office.com/people/")
    keyboard.keys(key.enter)
    
    wait(2)
    
    keyboard.keys(key.shift, key.tab, repeat_times=8)
    keyboard.keys(key.down, repeat_times=3)
    keyboard.keys(key.enter)
    
    end()