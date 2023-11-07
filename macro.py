from DesktopAutomationFramework import vars, keyboard, key, windows, files, input, Macro, wait, end

@Macro(interval_s=2.5) # You can increase this while testing and decrease later
def macro():
    v = vars.getNumber("ab", accepted_values=[2, 1.2, 6])
    input.message(str(v))

macro()
