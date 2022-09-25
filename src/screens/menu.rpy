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

    transform soh_buttons_enter:
        xalign 0.1 alpha 0.0 yalign 1.2

        ease 1 alpha 1.0 yalign 0.9

    transform half_opacity:
        alpha 0.5

    image bg default_background = Solid("#101010")

    $ soh_menu_buttons = 'mods/soh-desktop/res/img/misc/menu/buttons/' + persistent.soh_config['locale'] + '/'
    $ soh_menu_buttons_delocaled = 'mods/soh-desktop/res/img/misc/menu/buttons/'

    $ soh_dust_particles = SnowBlossom("mods/soh-desktop/res/img/misc/menu/dust_particle.png",
        count=10, fast=False,
        xspeed=(20, 50), yspeed=(100, -200), start=0, horizontal=False)
    $ soh_dust_particles1 = SnowBlossom("mods/soh-desktop/res/img/misc/menu/dust_particle.png",
        count=25, fast=False,
        xspeed=(34, 60), yspeed=(100, -200), start=0, horizontal=False)

    python:
        import os
        soh_system = os.uname()[0]

        def open_moddir():
            if os.path.exists('game/mods/soh-desktop'):
                os.system('xdg-open game/mods/soh-desktop')
            elif os.path.exists('mods/soh-desktop/'):
                os.system('xdg-open mods/soh-desktop')
            else:
                os.system('xdg-open ' + config.basedir + '/mods/soh-desktop')
                return

# TODO: Implement message dialogs and confirm dialogs

label soh_main_menu:
    window hide

    scene bg black with dissolve
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound_loop fadeout 1.0

    $ soh_Toast(persistent.soh_locale['sysmsg']['demo-notice'], 'alert')
    $ renpy.pause(4, hard=True)

    if not persistent.soh_first_run:
        $ soh_Achievement(persistent.soh_locale['achievements']['ach-finnaly'], 'mythical')
        $ renpy.pause(6, hard=True)

    $ persistent.soh_first_run = True

    play music faroff fadein 2


    $ renpy.start_predict_screen("soh_main_menu_screen")
    $ renpy.start_predict_screen("soh_main_menu_about_screen")
    $ renpy.start_predict_screen("soh_main_menu_screen_buttons")
    $ renpy.start_predict_screen("soh_main_menu_credits")
    $ renpy.start_predict_screen("soh_main_menu_confirmation")

    $ persistent.sprite_time = 'night'
    $ prolog_time()
    $ renpy.block_rollback()

    $ renpy.pause(1, hard=True)

    scene bg default_background with dissolve2
    call screen soh_main_menu_screen


label soh_main_menu_exit:
    window hide

    scene bg default_background with dissolve2
    stop music fadeout 6

    $ renpy.stop_predict_screen("soh_main_menu_screen")
    $ renpy.stop_predict_screen("soh_main_menu_about_screen")
    $ renpy.stop_predict_screen("soh_main_menu_screen_buttons")
    $ renpy.stop_predict_screen("soh_main_menu_credits")
    $ renpy.stop_predict_screen("soh_main_menu_confirmation")

    $ renpy.pause(7)
    return


screen soh_main_menu_screen:
    tag menu
    modal True
    zorder 999

    add "mods/soh-desktop/res/img/misc/menu/background.jpg" at soh_dissolve
    add "mods/soh-desktop/res/img/misc/menu/layer-one.png" at soh_dissolve
    add soh_dust_particles1
    add "mods/soh-desktop/res/img/misc/menu/layer-zero.png" at soh_dissolve

    add soh_dust_particles

    add "mods/soh-desktop/res/img/misc/menu/ui-overlay.png" at soh_dissolve

    timer 1.0 action Function(soh_Toast, persistent.soh_locale['sysmsg']['recommend-to-use-keyboard'], 'alert')

    use soh_main_menu_screen_buttons

screen soh_main_menu_screen_buttons:
    modal True tag menu

    key "K_ESCAPE" action [Play("sound", "mods/soh-desktop/res/sfx/ui/cancel.ogg"), ShowMenu("soh_main_menu_confirmation")]
    key "x" action Jump('soh_devroom')

    vbox xalign 0.1 yalign 0.9:
        imagebutton auto soh_menu_buttons + "start_%s.png":
            action [Hide("soh_main_menu_screen_buttons", dissolve), Hide("soh_main_menu_screen", Dissolve(8)), Jump("soh_chapter1_prologue_RU")]
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            at soh_dissolve

        imagebutton auto soh_menu_buttons + "settings_%s.png":
            action ShowMenu("soh_main_menu_settings")
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            at soh_dissolve

        imagebutton auto soh_menu_buttons + "other_%s.png":
            action ShowMenu("soh_main_menu_about_screen")
            mouse 'help'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            at soh_dissolve

        imagebutton auto soh_menu_buttons + "exit_%s.png":
            action ShowMenu("soh_main_menu_confirmation")
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/dialog.oga'
            at soh_dissolve
        at soh_buttons_enter


screen soh_main_menu_about_screen:
    modal True tag menu
    zorder 999

    add "mods/soh-desktop/res/img/misc/menu/settings/background.jpg" at soh_dissolve
    add "mods/soh-desktop/res/img/misc/menu/settings/layer-one.png" at soh_dissolve
    add soh_dust_particles1 at soh_dissolve
    add "mods/soh-desktop/res/img/misc/menu/settings/layer-zero.png" at soh_dissolve

    add soh_dust_particles at soh_dissolve

    add "mods/soh-desktop/res/img/misc/menu/ui-overlay.png" at soh_dissolve

    key "K_ESCAPE" action [Play("sound", "mods/soh-desktop/res/sfx/ui/cancel.ogg"), Return()]

    vbox xalign 0.1 yalign 0.9:
        imagebutton auto soh_menu_buttons + 'other/github_%s.png':
            action OpenURL("https://github.com/nitrogenez/shard-of-humanity")
            mouse 'link'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        imagebutton auto soh_menu_buttons + 'other/credits_%s.png':
            action ShowMenu("soh_main_menu_credits")
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

screen soh_main_menu_credits:
    tag menu
    modal True
    zorder 999

    key "K_ESCAPE" action [Play("sound", "mods/soh-desktop/res/sfx/ui/cancel.ogg"), Return()]

    add 'mods/soh-desktop/res/img/misc/menu/credits/background.jpg'
    add 'mods/soh-desktop/res/img/misc/menu/credits/alice.png' at soh_dissolve
    add soh_dust_particles
    add 'mods/soh-desktop/res/img/misc/menu/credits/credits.png' at soh_dissolve
    add 'mods/soh-desktop/res/img/misc/menu/credits/stopwar.png' at soh_dissolve

screen soh_main_menu_confirmation:
    tag menu modal True

    add im.Grayscale(im.Blur("mods/soh-desktop/res/img/misc/menu/background.jpg", 2.5))
    add im.Grayscale(im.Blur("mods/soh-desktop/res/img/misc/menu/layer-one.png", 2.7))
    add soh_dust_particles1
    add im.Grayscale(im.Blur("mods/soh-desktop/res/img/misc/menu/layer-zero.png", 2.9))
    add soh_dust_particles

    add Solid('#101010') at half_opacity
    add 'mods/soh-desktop/res/img/misc/menu/credits/stopwar.png'

    key "K_ESCAPE" action [Play("sound", "mods/soh-desktop/res/sfx/ui/cancel.ogg"), Return()]

    vbox xalign 0.45 yalign 0.5:
        imagebutton auto soh_menu_buttons + "quitconfirm/system_%s.png":
            action Quit(confirm=False)
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            mouse 'pointer'

        imagebutton auto soh_menu_buttons + "quitconfirm/gamemenu_%s.png":
            action Start("soh_main_menu_exit")
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            mouse 'pointer'

        imagebutton auto soh_menu_buttons + "quitconfirm/cancel_%s.png":
            action Return()
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
            mouse 'pointer'
