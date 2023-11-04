# Library Entrypoint / Expose library functionality

## Automation Functionality
from .automation.Windows import windows
from .automation.Keyboard import keyboard
from .automation.Input import input

from .automation.Variables import vars
from .automation.Common import wait, end

## Framework Functionality
from .framework.Decorators.MacroDecorator import Macro

## External Libraries w/ transparent access
from pynput.keyboard import Key