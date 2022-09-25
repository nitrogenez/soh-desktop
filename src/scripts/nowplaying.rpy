init python:
    track_metadata = {
        'mods/soh-desktop/res/music/4lienetic-far-off.ogg': '4Lienetic-Far Off',
        'mods/soh-desktop/res/music/blow-with-the-fires-lo-fi.ogg': 'Lunevski-Blow With The Fires (LoFi Remix)',
        'mods/soh-desktop/res/music/blow-with-the-fires-melis.ogg': 'Melis-Blow With The Fires (Remix)'
    }

    def soh_display_nowplaying():
        if persistent.soh_config['show-now-playing']:
            is_playing = renpy.music.is_playing(channel='music')

            if is_playing:
                what_playing = renpy.music.get_playing(channel='music')

                if what_playing not in track_metadata:
                    return Text('{b}Unknown{/b} - {i}Unnamed{/i}'), 0.1,

                else:
                    formatted = track_metadata[what_playing]
                    formatted = formatted.split('-')

                    return Text('{b}%s{/b} - {i}%s{/i}' % (formatted[0], formatted[1])), 0.1,
            else:
                return
        else:
            return

    renpy.image('soh_nowplaying_displayable', DynamicDisplayable(soh_display_nowplaying))

screen soh_nowplaying:
    modal False
    add 'soh_nowplaying_displayable'
