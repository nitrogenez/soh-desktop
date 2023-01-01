screen soh_main_menu_settings:
    modal True tag menu

    add "mods/soh-desktop/res/img/misc/menu/settings/background.jpg"
    add "mods/soh-desktop/res/img/misc/menu/settings/layer-one.png"
    add soh_dust_particles1
    add "mods/soh-desktop/res/img/misc/menu/settings/layer-zero.png"

    add soh_dust_particles

    add "mods/soh-desktop/res/img/misc/menu/ui-overlay.png"

    use soh_mm_settings_page1

screen soh_mm_settings_page1:
    modal True tag menu

    vbox pos (58, 688):
        textbutton persistent.soh_locale["menu-settings"]["nowplaying"]:
            action ToggleDict(persistent.soh_config, 'show-now-playing', True, False)
            mouse 'pointer'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/cancel.ogg'

            text_color '#808080'

            if persistent.soh_config['show-now-playing']:
                text_color '#6ae6d1'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style" text_style "soh_textbutton_style_text"

        textbutton persistent.soh_locale["menu-settings"]["moddir"]:
            action Function(open_moddir)
            mouse 'link'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style" text_style "soh_textbutton_style_text"

        textbutton persistent.soh_locale["menu-settings"]["github.issue"]:
            action OpenURL("https://github.com/nitrogenez/soh-desktop/issues")
            mouse 'link'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style"
            text_style "soh_textbutton_style_text"

        textbutton persistent.soh_locale["actions"]["back"]:
            action Return()
            mouse 'pointer'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/cancel.ogg'

            style "soh_textbutton_style"
            text_style "soh_textbutton_style_text"


    vbox xalign 0.9 ypos 688:
        textbutton persistent.soh_locale["languages"]["uk_UA"]:
            action [
                Function(soh_LoadLocale, "uk_UA"),
                Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])
            ]
            mouse 'pointer'

            if persistent.soh_config['locale'] == "uk_UA":
                text_color '#808080'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style" text_style "soh_textbutton_style_text"

        textbutton persistent.soh_locale["languages"]["en_US"]:
            action [
                Function(soh_LoadLocale, "en_US"),
                Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])
            ]
            mouse 'pointer'

            if persistent.soh_config['locale'] == "en_US":
                text_color '#808080'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style" text_style "soh_textbutton_style_text"

        textbutton persistent.soh_locale["languages"]["ru_RU"]:
            action [
                Function(soh_LoadLocale, "ru_RU"),
                Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])
            ]
            mouse 'pointer'

            if persistent.soh_config['locale'] == "ru_RU":
                text_color '#808080'

            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            style "soh_textbutton_style" text_style "soh_textbutton_style_text"

