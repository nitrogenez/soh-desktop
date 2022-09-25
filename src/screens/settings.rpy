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

    vbox xalign 0.1 yalign 0.9:

        if persistent.soh_config['show-now-playing']:
            imagebutton auto soh_menu_buttons + "settings/nowplaying_%s.png":
                action [ToggleDict(persistent.soh_config, 'show-now-playing', True, False),
                    Function(soh_Toast, 'ShowNowPlaying - False')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        elif not persistent.soh_config['show-now-playing']:
            imagebutton auto soh_menu_buttons + "settings/nowplaying_disabled_%s.png":
                action [ToggleDict(persistent.soh_config, 'show-now-playing', True, False),
                    Function(soh_Toast, 'ShowNowPlaying - True')]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        imagebutton auto soh_menu_buttons + "settings/moddir_%s.png":
            action Function(open_moddir)
            mouse 'pointer'
            hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
            activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

    vbox xalign 0.9 yalign 0.9:
        if persistent.soh_config['locale'] != 'uk_UA':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ua_%s.png":
                action [Function(soh_LoadLocale, 'uk_UA'), Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
        elif persistent.soh_config['locale'] == 'uk_UA':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ua_selected_%s.png":
                action NullAction()
                mouse 'default'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        if persistent.soh_config['locale'] != 'en_US':
            imagebutton auto soh_menu_buttons_delocaled + "lc_en_%s.png":
                action [Function(soh_LoadLocale, 'en_US'), Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
        elif persistent.soh_config['locale'] == 'en_US':
            imagebutton auto soh_menu_buttons_delocaled + "lc_en_selected_%s.png":
                action NullAction()
                mouse 'default'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        if persistent.soh_config['locale'] != 'ru_RU':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ru_%s.png":
                action [Function(soh_LoadLocale, 'ru_RU'), Function(soh_Toast, persistent.soh_locale['sysmsg']['locale-change-notice'])]
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'

        elif persistent.soh_config['locale'] == 'ru_RU':
            imagebutton auto soh_menu_buttons_delocaled + "lc_ru_selected_%s.png":
                action NullAction()
                mouse 'pointer'
                hover_sound 'mods/soh-desktop/res/sfx/ui/selected-button.ogg'
                activate_sound 'mods/soh-desktop/res/sfx/ui/pressed-button.ogg'
