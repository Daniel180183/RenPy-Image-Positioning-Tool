
init offset = 100

init:
    $ slot = 0
    $ start_search_menu = False
    $ start_image_pos_tool = False

default persistent.dialogueBoxOpacity = 0.9


# --- CHOICES / AUSWAHLMENÜ ---
screen choice(items):
    style_prefix "ipt_choice"

    window:
        style "ipt_window"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 5
            for caption, action, chosen in items:
                if action:
                    if "(locked)" in caption:
                        $ caption = caption.replace("(locked)", "")
                        button:
                            action None
                            style "ipt_button"
                            text caption style "ipt_button_text"
                    else:
                        button:
                            action action
                            style "ipt_button"
                            text caption style "ipt_button_text"
                else:
                    text caption style "ipt_text"


# --- INPUT ---
screen input(prompt):
    window:
        style "ipt_window"
        vbox:
            text prompt style "ipt_text"
            input id "input" style "ipt_text" color "#00008b"

    use ipt_quick_menu


# --- HAUPTMENÜ ---
screen main_menu():
    tag menu

    add ("ingame_background")

    frame:
        background Solid("#77c966")
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 15

            text "[project_name] v[project_version]":
                style "ipt_text"
                size 24
                color "#4f7649"
                xalign 0.5

            if renpy.android:
                textbutton _("Install {b}Image Positioning Tool{/b} in your project"):
                    action [
                        SetVariable("start_image_pos_tool", False),
                        SetVariable("start_search_menu", True),
                        Start()
                    ] style "ipt_button" text_style "ipt_center_button_text"

                textbutton _("Test {b}Image Positioning Tool{/b}"):
                    action [
                        SetVariable("start_search_menu", False),
                        SetVariable("start_image_pos_tool", True),
                        Start()
                    ] style "ipt_button" text_style "ipt_center_button_text"
            else:
                textbutton _("Install {b}Image Positioning Tool{/b} in your project"):
                    action [
                        SetVariable("start_image_pos_tool", False),
                        SetVariable("start_search_menu", True),
                        Start()
                    ] style "ipt_button" text_style "ipt_center_button_text"

                textbutton _("Test {b}Image Positioning Tool{/b}"):
                    action [
                        SetVariable("start_search_menu", False),
                        SetVariable("start_image_pos_tool", True),
                        Start()
                    ] style "ipt_button" text_style "ipt_center_button_text"

                textbutton _("Quit"):
                    action Quit(confirm=False) style "ipt_button" text_style "ipt_center_button_text"


# --- QUICK MENU ---
screen ipt_quick_menu():
    hbox:
        xalign 1.0
        yalign 1.0
        spacing 5

        if renpy.android:
            textbutton _("Back") action Rollback() style "ipt_button" text_style "ipt_button_text"
            textbutton _("Skip") action Skip() style "ipt_button" text_style "ipt_button_text"
            textbutton _("F.Skip") action Skip(fast=True, confirm=True) style "ipt_button" text_style "ipt_button_text"
            textbutton _("Auto") action Preference("auto-forward", "toggle") style "ipt_button" text_style "ipt_button_text"
        else:
            textbutton _("Back") action Rollback() style "ipt_button" text_style "ipt_button_text"
            textbutton _("Save") action ShowMenu('save') style "ipt_button" text_style "ipt_button_text"
            textbutton _("Skip") action Skip() style "ipt_button" text_style "ipt_button_text"
            textbutton _("F.Skip") action Skip(fast=True, confirm=True) style "ipt_button" text_style "ipt_button_text"
            textbutton _("Auto") action Preference("auto-forward", "toggle") style "ipt_button" text_style "ipt_button_text"
            textbutton _("Prefs") action ShowMenu('preferences') style "ipt_button" text_style "ipt_button_text"


# --- Beenden Abfrage ---
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    # Dunkler Hintergrund-Overlay
    add Solid("#00000088")

    frame:
        background Solid("#2e4a2a") # Rahmenfarbe (Dunkelgrün)
        padding (1, 1, 1, 1)
        align (0.5, 0.5)

        frame:
            background Solid("#1e1e1e") # Fensterhintergrund
            padding (20, 20, 20, 20)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15

                label _(message):
                    style "ipt_text"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 70

                    textbutton _("Yes"):
                        action yes_action
                        style "ipt_button"
                        text_style "ipt_button_text"

                    textbutton _("No"):
                        action no_action
                        style "ipt_button"
                        text_style "ipt_button_text"


