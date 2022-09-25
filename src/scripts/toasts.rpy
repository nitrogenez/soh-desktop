init:
    default available_screens = ['soh_toast_1', 'soh_toast_2', 'soh_toast_3', 'soh_toast_4', 'soh_toast_5', 'soh_toast_6', 'soh_toast_7']
    default delay_end = True

init python:

    # android's toast implementation
    def soh_Toast(text='...', level='default'):
        global available_screens
        global delay_end

        toasted = False
        while not toasted:
            if delay_end and len(available_screens) > 0:
                sc_name = available_screens[0]
                available_screens.remove(sc_name)

                renpy.play('mods/soh-desktop/res/sfx/toast/toast-%s.oga' % (level), channel='sound')

                renpy.show_screen(sc_name, text, level)
                toasted = True
                delay_end = False

            else:
                renpy.pause(delay=0.1)

    def soh_ToastRefresh(screen_name):
        renpy.hide_screen(screen_name)
        global available_screens
        available_screens.append(screen_name)


# style for toasts
style soh_toasts:
    background Frame("mods/soh-desktop/res/img/ui/toasts/toastbox.png", 10, 10)
    xpadding 15 ypadding 15

style soh_alerts:
    background Frame("mods/soh-desktop/res/img/ui/toasts/toastbox_alert.png", 10, 10)
    xpadding 15 ypadding 15

style soh_toast_text:
    font 'mods/soh-desktop/res/fonts/SF-Pro-Display-Regular.otf'
    size 26

# transform for toasts
transform soh_toast_t:
    xalign 0.5 yalign -0.2 alpha 0.0

    # inertia effect
    ease 0.2 yalign 0.1 alpha 1.0
    ease 0.1 yalign 0.12
    ease 0.05 yalign 0.08

    pause 4
    linear 1.0 alpha 0.0

# screens for toasts
screen soh_toast_1(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_1")
    timer 0.5 action SetVariable('delay_end', True)


screen soh_toast_2(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_2")
    timer 0.5 action SetVariable('delay_end', True)

screen soh_toast_3(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_3")
    timer 0.5 action SetVariable('delay_end', True)

screen soh_toast_4(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_4")
    timer 0.5 action SetVariable('delay_end', True)

screen soh_toast_5(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_5")
    timer 0.5 action SetVariable('delay_end', True)

screen soh_toast_6(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_6")
    timer 0.5 action SetVariable('delay_end', True)

screen soh_toast_7(toast_text, level):
    zorder 999 modal False
    frame:
        if level != 'alert':
            style "soh_toasts"
        else:
            style "soh_alerts"
        text toast_text style "soh_toast_text"
        at soh_toast_t
    timer 6.0 action Function(soh_ToastRefresh, "soh_toast_7")
    timer 0.5 action SetVariable('delay_end', True)