from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end, pause

@Macro()
def macro():
    gui.show(vars.getString("a"))
    
    v1 = gui.options("a", "b")
    v2 = gui.options("stock_ej_report", "stock_1", "stock_2")
    
    gui.show("You chose 1: " + v1)
    gui.show("You chose 2: " + v2)
    
    end()