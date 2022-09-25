init:
    default delay_end_achievements = True
    default available_screens_achievements = ['soh_achievement_1']

init python:

    # soh_Toast is a base
    def soh_Achievement(text='...', level='default'):
        global available_screens_achievements
        global delay_end_achievements

        toasted = False
        while not toasted:
            if delay_end_achievements and len(available_screens_achievements) > 0:
                sc_name = available_screens_achievements[0]
                available_screens_achievements.remove(sc_name)

                renpy.play('mods/soh-desktop/res/sfx/ach/ach-%s.ogg' % (level), channel='sound')
                renpy.show_screen(sc_name, text, level)
                toasted = True
                delay_end_achievements = False

            else:
                renpy.pause(delay=0.1)

    def soh_AchievementRefresh(screen_name):
        renpy.hide_screen(screen_name)
        global available_screens_achievements
        available_screens_achievements.append(screen_name)


# style for achievements
style soh_achievements:
    background Frame("mods/soh-desktop/res/img/ui/achievements/achbox.png")
    xpadding 15 ypadding 15

style soh_achievements_rare:
    background Frame("mods/soh-desktop/res/img/ui/achievements/achbox_r.png")
    xpadding 15 ypadding 15

style soh_achievements_mythical:
    background Frame("mods/soh-desktop/res/img/ui/achievements/achbox_m.png")
    xpadding 15 ypadding 15

style soh_achievements_text:
    font 'mods/soh-desktop/res/fonts/SF-Pro-Display-Regular.otf'
    size 28
style soh_achievements_text_mythical:
    font 'mods/soh-desktop/res/fonts/SF-Pro-Display-Regular.otf'
    size 28
    color '#d1af8a'

# transform for achievements
transform soh_achievement_t_icon:
    xalign 0.5 yalign 0.4 zoom 0.0

    ease 0.2 zoom 1 
    ease 0.1 zoom 0.8
    ease 0.1 zoom 1

    ease 1 yalign 0.4 zoom 1.2
    pause 0.4
    ease 1 yalign 0.05 zoom 0.8

    pause 5
    linear 1.0 alpha 0.0

transform soh_achievement_t_level:
    xalign 0.1 yalign -0.2 zoom 0.0

    ease 1 yalign 0.1 zoom 0.8
    pause 3

    linear 1.0 alpha 0.0

transform soh_achievement_t:
    xalign 0.5 yalign 0.55 zoom 0.0

    ease 1 yalign 0.55 zoom 1.0
    pause 0.4
    ease 1 yalign 0.15 zoom 0.8

    pause 5
    linear 1.0 alpha 0.0


screen soh_achievement_1(ach_text, level):
    zorder 999 modal False

    add 'mods/soh-desktop/res/img/ui/achievements/icon.png' at soh_achievement_t_icon
    
    frame:
        style 'soh_toasts'

        text persistent.soh_locale['achievements'][level + '-achievement-unlocked'] style 'soh_achievements_text'
        at soh_achievement_t_level

    frame:
        if level == 'mythical':
            style 'soh_achievements_mythical'
        elif level == 'rare':
            style 'soh_achievements_rare'
        else:
            style 'soh_achievements'

        if level == 'mythical':
            text ach_text style 'soh_achievements_text_mythical'
        else:
            text ach_text style 'soh_achievements_text'
        at soh_achievement_t

    timer 8.5 action Function(soh_AchievementRefresh, "soh_achievement_1")
    timer 0.5 action SetVariable("delay_end", True)
