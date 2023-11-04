from .DesktopAutomationFramework import keyboard, input, windows, vars, Macro, Key, wait, end

@Macro(interval_s=1)
def macros():
    # while True:
    #     print(vars.time.second)
    #     time.sleep(1)
    
    print(vars.time.strftime("%d-%m-%Y %H:%M:%S"))
    end()

    option = input.optionMenu("variante 1", "variante 2", "variante 3", stop_if_no_selection=True)

    if option == "variante1":
        # Do this
        pass
    else:
        # Do that        
        pass

    keyboard.keys(Key.ctrl, Key.alt, Key.tab)
    keyboard.keys(Key.right, repeat_times=2, repeat_interval_s=1)

    result = input.confirm("Do you want to continue?", buttons=(input.YES, input.NO))
    if result != input.YES:
        exit()

    keyboard.keys(Key.cmd)
    if True:
        keyboard.write("two")
    keyboard.keys(Key.cmd)
    keyboard.write("three")

macros()