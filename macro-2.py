from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end, pause

@Macro()
def macro():
    name = gui.ask("name: ")
    gui.show(1)
    gui.show(name)
    gui.show(3)
    
    end()