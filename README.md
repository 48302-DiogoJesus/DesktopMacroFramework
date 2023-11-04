# Features
- Create macros using normal python scripts
- Monitor window to visualize macro in real-time
  - start/pause/resume/stop macro
  - schedule macro execution for later
- Produces Logs

Install library (from github)

`pip install --upgrade --force-reinstall git+https://github.com/48302-DiogoJesus/DesktopMacroFramework`

Use library in your python files

```python
from DesktopAutomationFramework import keyboard, input, windows, vars, Macro

# 1. Define the Macro
@Macro(interval_s=1)
def macro():
  keyboard.keys(Key.alt)

# 2. Execute the Macro
macro()
```