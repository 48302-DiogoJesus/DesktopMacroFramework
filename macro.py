from DesktopAutomationFramework import vars, keyboard, key, windows, files, input, Macro, wait, end

@Macro(interval_s=2.5) # You can increase this while testing and decrease later
def macro():
    v = vars.getString("v", accepted_values=["hello word", "joe"])
    input.message(v)

macro()
