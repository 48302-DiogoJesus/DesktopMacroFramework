from DesktopAutomationFramework import keyboard, key, windows, vars, gui, key, Macro, wait, end

@Macro(interval_s=1)
def macro():
    variante = gui.options("stock_ej_report", "stock_1", "stock_2")
    
    gui.show("You chose: " + variante)
    
    # end()

macro()
