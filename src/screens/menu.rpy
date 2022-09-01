# Copyright (C) 2022 nitrogenez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

init:
    transform soh_dissolve:
        alpha 0.0
        linear 6.0 alpha 1.0

    image bg default_background = Solid("#101010")


label soh_main_menu:
    window hide

    scene bg black with dissolve
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound_loop fadeout 1.0

    $ renpy.start_predict_screen("soh_main_menu_screen")
    $ renpy.start_predict_screen("soh_main_menu_about_screen")

    $ persistent.sprite_time = 'night'
    $ night_time()
    $ renpy.block_rollback()

    $ renpy.pause(1, hard=True)
    scene bg default_background with dissolve2

    call screen soh_main_menu_screen
    play music blow_with_the_fires_melis fadein 2

screen soh_main_menu_screen:
    tag menu
    modal True
    zorder 999

    add CursorParallax("mods/"+SOH_VARIANT+"/res/img/misc/menu/background.jpg", 10) at soh_dissolve
    add CursorTracker("mods/"+SOH_VARIANT+"/res/img/misc/menu/layer-one.png", 15) at soh_dissolve:
        xpos 809
        ypos 462
    add CursorTracker("mods/"+SOH_VARIANT+"/res/img/misc/menu/layer-zero.png", 13) at soh_dissolve:
        xpos 1180
        ypos 316
    
    add "mods/"+SOH_VARIANT+"/res/img/misc/menu/title.png" at soh_dissolve

    imagemap:
        alpha False
        idle "mods/"+SOH_VARIANT+"/res/img/misc/menu/ui-main.png"
        hover "mods/"+SOH_VARIANT+"/res/img/misc/menu/ui-main-hover.png"

        hotspot (38, 859, 428, 33) action (Hide("soh_main_menu_screen", dissolve), Jump("soh_chapter1_prologue"))
        hotspot (35, 910, 421, 41) action ShowMenu("soh_main_menu_about_screen")
        hotspot (37, 956, 158, 42) action Return()

screen soh_main_menu_about_screen:
    tag menu
    modal True
    zorder 999

    imagemap:
        alpha False
        idle "mods/"+SOH_VARIANT+"/res/img/misc/menu/ui-about.png"
        hover "mods/"+SOH_VARIANT+"/res/img/misc/menu/ui-about-hover.png"

        hotspot (37, 884, 359, 35) action OpenURL("https://github.com")
        hotspot (37, 937, 187, 35) action Return()
