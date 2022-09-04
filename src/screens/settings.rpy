screen soh_main_menu_settings:
    modal True tag menu

    add CursorParallax("mods/soh-desktop/res/img/misc/menu/settings/background.jpg", 10)
    add CursorParallax("mods/soh-desktop/res/img/misc/menu/settings/layer-one.png", 15)
    add CursorParallax(soh_dust_particles1, 10)
    add CursorParallax("mods/soh-desktop/res/img/misc/menu/settings/layer-zero.png", 13)

    add CursorParallax(soh_dust_particles, 8)

    add "mods/soh-desktop/res/img/misc/menu/ui-overlay.png"

    use soh_mm_settings_page1

screen soh_mm_settings_page1:
    modal True tag menu

    vbox xalign 0.1 yalign 0.9:

        if persistent.soh_config['show-now-playing']:
            imagebutton auto soh_menu_buttons + "settings/nowplaying_%s.png":
                action [ToggleDict(persistent.soh_config, 'show-now-playing', True, False),
                    Function(soh_toast, 'ShowNowPlaying - False')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        elif not persistent.soh_config['show-now-playing']:
            imagebutton auto soh_menu_buttons + "settings/nowplaying_disabled_%s.png":
                action [ToggleDict(persistent.soh_config, 'show-now-playing', True, False),
                    Function(soh_toast, 'ShowNowPlaying - True')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        imagebutton auto soh_menu_buttons + "settings/sound_%s.png":
            action NullAction()
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        imagebutton auto soh_menu_buttons + "settings/moddir_%s.png":
            action Function(open_moddir)
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        hbox:
            imagebutton auto soh_menu_buttons_delocaled + "btn_prev_%s.png":
                action NullAction()
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

            imagebutton auto soh_menu_buttons_delocaled + "btn_next_%s.png":
                action NullAction()
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

    vbox xalign 0.9 yalign 0.9:
        if persistent.soh_config['locale'] != 'ua':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ua_%s.png":
                action [SetDict(persistent.soh_config, 'locale', 'ua'), Function(soh_toast, 'Мова буде змінена після перезаходження')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
        elif persistent.soh_config['locale'] == 'ua':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ua_selected_%s.png":
                action NullAction()
                mouse 'default'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        if persistent.soh_config['locale'] != 'en':
            imagebutton auto soh_menu_buttons_delocaled + "lc_en_%s.png":
                action [SetDict(persistent.soh_config, 'locale', 'en'), Function(soh_toast, 'Language will be changed after reloading the game')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
        elif persistent.soh_config['locale'] == 'en':
            imagebutton auto soh_menu_buttons_delocaled + "lc_en_selected_%s.png":
                action NullAction()
                mouse 'default'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        if persistent.soh_config['locale'] != 'ru':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ru_%s.png":
                action [SetDict(persistent.soh_config, 'locale', 'ru'), Function(soh_toast, 'Язык будет изменён после перезахода')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        elif persistent.soh_config['locale'] == 'ru':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ru_selected_%s.png":
                action NullAction()
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
