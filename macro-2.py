from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end

@Macro(interval_s=2)
def macro():
    v1 = gui.options("a", "b")
    v2 = gui.options("stock_ej_report", "stock_1", "stock_2")
    
    gui.show("You chose 1: " + v1)
    gui.show("You chose 2: " + v2)
    
    end()