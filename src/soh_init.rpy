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


init 1:
    define SOH_VARIANT = "soh-desktop"  # initialize mod variant
    define SOH_VERSION = SOH_VARIANT + "-0.0.1"
    define SOH_DISPLAYNAME = u"Осколок человечности"

    # define essential directories
    define SOH_ROOT = "mods/" + SOH_VARIANT
    define SOH_RESOURCES = "mods/" + SOH_VARIANT + "/res"

    # define resources directories
    define SOH_IMAGES = SOH_RESOURCES + "/img"
    define SOH_BG = SOH_IMAGES + "/bg"
    define SOH_CG = SOH_IMAGES + "/cg"
    define SOH_ANIM = SOH_IMAGES + "/anim"
    define SOH_SPR = SOH_IMAGES + "/sprites"
    define SOH_MISC = SOH_IMAGES + "/misc"
    
    define SOH_FONTS = SOH_RESOURCES + "/fonts"

    define SOH_MUSIC = SOH_RESOURCES + "/music"
    define SOH_SFX = SOH_RESOURCES + "/sfx"
    define SOH_AMBIENCE = SOH_RESOURCES + "/ambience"

    define SOH_START = "soh_main_menu"

    image soh_title_text = ParameterizedText(font='mods/soh-desktop/res/fonts/SF-Pro-Display-Black.otf', size=76)

init 1 python:
    import socket
    import os
    import json

    persistent.soh_locale = []      # locale texts
    soh_lc_stream = None            # locale file stream 

    persistent.soh_first_run = False

    persistent.soh_config = {
        'locale': 'uk_UA',              # locale
        'show-now-playing': False,      # now playing screen
        'cursor-theme': 'Vimix-cursors' # in-game cursor theme (Vimix by default)
    }
    persistent.soh_achievements = []

    config.mouse = {
        'default': [(SOH_MISC+'/cursors/%s/src/default.png' % (persistent.soh_config['cursor-theme']), 0, 0)],
        'link':    [(SOH_MISC+'/cursors/%s/src/link.png' % (persistent.soh_config['cursor-theme']), 0, 0)],
        'help':    [(SOH_MISC+'/cursors/%s/src/help.png' % (persistent.soh_config['cursor-theme']), 0, 0)],
        'pointer': [(SOH_MISC+'/cursors/%s/src/pointer.png' % (persistent.soh_config['cursor-theme']), 0, 0)],
        'right':   [(SOH_MISC+'/cursors/%s/src/right_ptr.png' % (persistent.soh_config['cursor-theme']), 0, 0)]
    }
    default_mouse = 'default'

    if socket.gethostname() == 'neuralist-arch':
        config.developer = True
        config.autoreload = True

    def soh_LoadLocale(locale):
        persistent.soh_config['locale'] = locale

        soh_lc_stream = renpy.file('mods/soh-desktop/res/locale/' + locale + '.json')
        persistent.soh_locale = json.load(soh_lc_stream)
        soh_lc_stream.close()

    soh_mod_files = []

    def soh_CheckSystemLocale():
        if os.name == 'posix':
            lang = os.getenv('LANG').replace('.UTF-8', '')

            if lang != None and lang != 'C':
                soh_LoadLocale(lang)
            else:
                soh_LoadLocale('uk_UA')

        else:
            import ctypes
            import locale

            windll = ctypes.windll.kernel32
            soh_LoadLocale(locale.windows_locale[windll.GetUserDefaultUiLanguage()])

        if persistent.soh_config['locale'] == None:
            return 1
        return 0


    for i in renpy.list_files():
        if i.startswith(SOH_ROOT):
            soh_mod_files.append(i)

    if soh_CheckSystemLocale() == 1:
        persistent.soh_config['locale'] = 'uk_UA'

    soh_LoadLocale(persistent.soh_config["locale"])

    mods[SOH_START] = persistent.soh_locale['modname']

    # try to show mod thumbnail in menu
    try:
        modsImages[SOH_START] = (SOH_MISC + "mod_thumbnail_320x180.jpg", False, SOH_START)
    except:
        pass