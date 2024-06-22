from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end, pause

@Macro()
def macro():
    
    keyboard.keys(key.win, "r")
    keyboard.write(vars.user_dir)
    keyboard.keys(key.enter)
    
    windows.wait("Diogo")
    
    keyboard.keys(key.alt)
    keyboard.keys(key.enter)
    keyboard.keys(key.down, repeat_times=12)
    
    
    
    
    end()