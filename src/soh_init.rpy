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

    python:
        import socket
        if socket.gethostname() == 'greatdeceiver':
            config.developer = True
            config.autoreload = True

    $ config.mouse = {
        'default': [(SOH_MISC+'/cursors/Vimix-cursors/src/default.png', 0, 0)],
        'link':    [(SOH_MISC+'/cursors/Vimix-cursors/src/link.png', 0, 0)],
        'help':    [(SOH_MISC+'/cursors/Vimix-cursors/src/help.png', 0, 0)],
        'pointer': [(SOH_MISC+'/cursors/Vimix-cursors/src/pointer.png', 0, 0)],
        'right':   [(SOH_MISC+'/cursors/Vimix-cursors/src/right_ptr.png', 0, 0)]
    }
    $ default_mouse = 'default'

    python:
        mods[SOH_START] = SOH_DISPLAYNAME

        # try to show mod thumbnail in menu
        try:
            modsImages[SOH_START] = (SOH_MISC + "mod_thumbnail_320x180.jpg", False, SOH_START)
        except:
            pass