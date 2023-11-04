# Library Entrypoint / Expose library functionality

## Automation Functionality
import automation.Windows as windows
import automation.Keyboard as keyboard
import automation.Input as input

from automation.Common import wait, end
import automation.Variables as vars

## Framework Functionality
from framework.Decorators.MacroDecorator import Macro

## External Libraries w/ transparent access
from pynput.keyboard import Key