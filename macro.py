from DesktopAutomationFramework import vars, keyboard, key, windows, files, gui, Macro, wait, end

@Macro(interval_s=1) # You can increase this while testing and decrease later
def macro():
    gui.message("1")
    gui.message("2")
    gui.message("3")
    gui.message("4")
    gui.message("5")
    gui.message("6")
    gui.message("7")
    gui.message("8")
    gui.message("9")
    
    if True:
        print("hey")
    else:
        print("ho")
    
    gui.message("10")
    gui.message("11")
    gui.message("12")
    gui.message("13")
    gui.message("14")
    gui.message("15")
    gui.message("16")
    gui.message("17")

macro()
