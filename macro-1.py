from DesktopAutomationFramework import vars, keyboard, key, windows, files, gui, Macro, wait, end

@Macro(interval_s=1) # You can increase this while testing and decrease later
def macro():
    gui.show("1")
    gui.show("2")
    gui.show("3")
    gui.show("4")
    gui.show("5")
    gui.show("6")
    gui.show("7")
    gui.show("8")
    gui.show("9")
    
    if True:
        print("hey")
    else:
        print("ho")
    
    gui.show("10")
    gui.show("11")
    gui.show("12")
    gui.show("13")
    gui.show("14")
    gui.show("15")
    gui.show("16")
    gui.show("17")
