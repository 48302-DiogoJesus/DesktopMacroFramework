from DesktopAutomationFramework import vars, keyboard, key, windows, files, input, Macro, wait, end

@Macro(interval_s=2.5) # You can increase this while testing and decrease later
def macro():

    v = vars.getString("s1", accepted_values=["one", "two", "three"])
    v = vars.getString("s2", ["one"])
    v = vars.getString("s3", ["one", "two"])
    v = vars.getString("s4")
    
    v = vars.getNumber("n1", accepted_values=[2, 1.2, 6])
    v = vars.getNumber("n2", [1.2])
    v = vars.getNumber("n3", [1.2, 2])
    v = vars.getNumber("n4")
    input.message(str(v))

macro()
