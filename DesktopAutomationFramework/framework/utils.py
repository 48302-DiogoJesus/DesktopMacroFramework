import inspect
from framework.types.MacroStatus import MacroStatus
from framework.Variables import RVariables, RWVariables

def handleMasterEventsWhileRunning(func, args):
    if RWVariables.stopMacro:
        RWVariables.stopMacro = False
        raise Exception("Macro Stopped")
    
    if not RVariables.resumeMacroFlag.is_set():
        print("[PAUSED] at", func.__name__, args)
        RWVariables.macroStatus = MacroStatus.PAUSED
        tryUpdateMacroStatusGUI()

    RVariables.resumeMacroFlag.wait()

    if RWVariables.stopMacro:
        RWVariables.stopMacro = False
        raise Exception("Macro Stopped")

    RWVariables.macroStatus = MacroStatus.RUNNING
    tryUpdateMacroStatusGUI()

def get_source_around_line(window_size=8):
    frame = inspect.currentframe()
    if frame is None: raise Exception("Could not get code from stackframe")
    
    # Go 2 layers down
    caller_frame = frame.f_back
    if caller_frame is None: raise Exception("Could not get code from stackframe")
    caller_frame= caller_frame.f_back
    if caller_frame is None: raise Exception("Could not get code from stackframe")
    
    source_lines, start_line = inspect.getsourcelines(caller_frame)
    # jump annotation + def <fun_name>()
    source_lines = source_lines[2:]
    start_line += 2

    line_idx_abs = caller_frame.f_lineno - start_line

    # Calculate the start and end line numbers for the window
    start_line = max(0, line_idx_abs - window_size // 2)
    end_line = min(len(source_lines), line_idx_abs + (window_size // 2) + 1)

    # Extract the lines within the window
    window_lines = source_lines[start_line:end_line]
    line_index_rel = line_idx_abs - start_line

    return window_lines, line_index_rel

def tryUpdateMacroStatusGUI():
    if RWVariables.macroMonitorShared is None: return
    RWVariables.macroMonitorShared.updateStatus(RWVariables.macroStatus)

def showMacroErrorGUI(error_msg: str):
    if RWVariables.macroMonitorShared is None: raise Exception("MacroMonitor not initialized")
    RWVariables.macroMonitorShared.setMessage("ERROR: " + error_msg)