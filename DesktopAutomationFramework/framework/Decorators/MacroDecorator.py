import datetime
import os
import subprocess
import sys
import threading

from ...automation.Common import end
from ..MacroMonitorGUI import MacroMonitorGUI
from ..types.MacroStatus import MacroStatus
from ..utils import showMacroErrorGUI, tryUpdateMacroStatusGUI
from ..Variables import RVariables, RWVariables

# Put on macro function
def Macro(interval_s: int):
    RWVariables.time_between_actions_s = interval_s

    # Start/Resume
    def onMacroStartResume():
        if RWVariables.macroStatus is MacroStatus.PAUSED or RWVariables.macroStatus is MacroStatus.READY:
            RVariables.resumeMacroFlag.set()
    def onMacroPause():
        if RWVariables.macroStatus is MacroStatus.RUNNING:
            RVariables.resumeMacroFlag.clear()
    def onMacroStop():
        if RWVariables.macroStatus is MacroStatus.RUNNING or RWVariables.macroStatus is MacroStatus.PAUSED:
            RWVariables.stopMacro = True
            if RWVariables.macroStatus is MacroStatus.PAUSED:
                # Make thread resume in order to realize it should stop
                RVariables.resumeMacroFlag.set()
    def onMacroSchedule(macroMonitor: MacroMonitorGUI, time: str):
        start_time = datetime.datetime.now() + datetime.timedelta(minutes=float(time))
        start_time_str = start_time.strftime("%H:%M:%S")
        start_time_str_name = start_time.strftime("%H-%M-%S")
        
        abs_script_location = os.path.abspath(sys.argv[0])
        args = ' '.join(sys.argv[1:])
        
        command = f"pythonw \"{abs_script_location}\" {args}"

        schtasks_command = f"schtasks /create /sc once /tn DesktopAutomation_{RVariables.macro_name}_{start_time_str_name} /tr \"{command}\" /st {start_time_str} /F"

        try:
            result = subprocess.run(schtasks_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Task scheduled successfully.")
            print("Command output:", result.stdout.decode())
            exit()
        except subprocess.CalledProcessError as e:
            print("Error scheduling task:", e.stderr.decode())
            macroMonitor.showPopup(f"Error scheduling task: {e.stderr.decode()}")
    
    def decorator(func):
        def wrapper():
            # Runs when macro() function is called
            def recursive_macro_runner(errored_on_previous_run: bool = False):
                try:
                    RVariables.logger.new_file()
                    RWVariables.macroStatus = MacroStatus.READY
                    if not errored_on_previous_run:
                        tryUpdateMacroStatusGUI()
                    else:
                        # Reset Error
                        errored_on_previous_run = False
                        # Leave the error message there
                        pass
                    print("[READY]")
                    
                    # Pause and wait until started
                    RVariables.resumeMacroFlag.clear()
                    RVariables.resumeMacroFlag.wait()
                    RWVariables.macroStatus = MacroStatus.RUNNING
                    print("[RUNNING]")
                    tryUpdateMacroStatusGUI()
                    # Call macro() function
                    func()
                except Exception as e:
                    errored_on_previous_run = True
                    error_message = str(e)
                    showMacroErrorGUI(error_message)
                    RVariables.logger.error(error_message)
                finally:
                    print("[FINISHED]")
                    # Call itself again
                    recursive_macro_runner(errored_on_previous_run)
            
            # Start Macro Runner Thread
            thread = threading.Thread(target=recursive_macro_runner)
            thread.daemon = True # If main thread dies it dies too
            thread.start()
            
            # ! Blocks the main thread on tkinter GUI
            RWVariables.macroMonitorShared = MacroMonitorGUI(RVariables.macro_name, onMacroStartResume, onMacroPause,  onMacroStop, onMacroSchedule) # type: ignore
            RWVariables.macroMonitorShared.launchGUI()
        return wrapper
    
    return decorator
