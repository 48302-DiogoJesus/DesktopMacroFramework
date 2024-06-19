import datetime
import inspect
import time
from typing import Any, Optional

from ..types.MacroStatus import MacroStatus
from ..utils import handleMasterEventsWhileRunning
from ..Variables import RWVariables, RVariables

# Put on Automation functions. Called for each function. E.g., once for wait()
def AutomationDecorator(func):
    # Useful to allow going back on instructions
    # Note: Identify a specific function call by its line number
    cachedReturnValues: dict[int, Optional[Any]] = {}
    
    def wrapper(*args, **kwargs):
        nonlocal cachedReturnValues
        handleMasterEventsWhileRunning(func, args)

        current_line = inspect.stack()[1].lineno
        hashcode = inspect.stack()[1]
        if RWVariables.macroStartLineNumber is not None and current_line < RWVariables.macroStartLineNumber: 
            return cachedReturnValues[current_line]
        
        if RWVariables.macroMonitorShared is None: raise Exception("Macro Monitor variable was not initialized (= None)")
        RWVariables.macroMonitorShared.updateInstruction(current_line)

        # Execute operation
        try:
            RVariables.logger.write(f"[CALL] {str(func.__module__).replace('DesktopAutomationFramework.', '')}.{func.__name__} {args}")
            result = func(*args, **kwargs)
            cachedReturnValues[current_line] = result
            # On success
            if result is not None:
                RVariables.logger.write(f"[RESULT] {result}")
        except Exception as e:
            # Logger (log event on error)
            RVariables.logger.error(f"{str(func.__module__).replace('DesktopAutomationFramework.', '')}.{func.__name__} {args} => Threw Exception")
            # Re-raise error
            raise e
        
        handleMasterEventsWhileRunning(func, args)

        # Time Between Actions (with a stop/pause check every 50 ms to improve responsiveness)
        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).total_seconds() < RWVariables.time_between_actions_s:
            time.sleep(0.05) # 50 ms
            handleMasterEventsWhileRunning(func, args)
        
        handleMasterEventsWhileRunning(func, args)
        return result
    return wrapper