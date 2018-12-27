"""Script that shows a little icon in the top-left corner when an exception happens."""

import time

from .luanamespace import *
from .lua import luafunction

__all__ = ['setup', 'show']

# Hide the error icon after n milliseconds
ICON_HIDE_DELAY = 5
error_icon, _ = Material('pygmod_error.png')
should_draw_icon = False
hide_icon_at = 0


def show():
    global should_draw_icon, hide_icon_at

    should_draw_icon = True
    hide_icon_at = time.clock() + ICON_HIDE_DELAY


def setup():
    def draw_pygmod_error_icon():
        global should_draw_icon

        if not should_draw_icon:
            return

        surface.SetDrawColor(255, 255, 255, 255)
        surface.SetMaterial(error_icon)
        surface.DrawTexturedRect(20, 20, 32, 32)

        if time.clock() > hide_icon_at:
            should_draw_icon = False

    hook.Add('DrawOverlay', 'pygmod_show_error_icon', luafunction(draw_pygmod_error_icon))
