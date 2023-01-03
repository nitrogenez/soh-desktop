init:
    $ soh_value_bar_null = Frame("mods/soh-desktop/res/img/ui/bar/base_null.png")
    $ soh_value_bar_full = Frame("mods/soh-desktop/res/img/ui/bar/base_full.png")


style soh_value_bar is bar:
    background None
    mouse 'pointer'

    thumb 'mods/soh-desktop/res/img/ui/bar/thumb.png'
    left_bar soh_value_bar_full
    right_bar soh_value_bar_null