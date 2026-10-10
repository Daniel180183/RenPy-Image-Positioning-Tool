
init offset = 100

define config.quit_action = Quit(confirm=True)

init python:

    # -------------------------------------------------------------
    # ISOLIERTE STYLES FÜR DAS TOOL DEFINIEREN (Präfix "ipt_")
    # -------------------------------------------------------------

    # 1. Isolierter Text-Style
    style.ipt_text = Style(style.default)
    style.ipt_text.font = "DejaVuSansMono.ttf"
    style.ipt_text.size = 14
    style.ipt_text.color = "#000000"

    # 2. Button-Style komplett isolieren (Kein Erben von style.button)

    # style.ipt_button = Style(style.default) # <- 'style.default' statt 'style.button'!

    style.ipt_button.background = Frame(Solid("#84ec6e"), 0, 0)
    style.ipt_button.hover_background = Frame(Solid("#92fb7b"), 0, 0)
    style.ipt_button.padding = (4, 1, 4, 1)
    style.ipt_button.xmaximum = 900
    style.ipt_button.align = (0.5, 0.5)

    style.ipt_pm_button.background = Frame(Solid("#84ec6e"), 0, 0)
    style.ipt_pm_button.hover_background = Frame(Solid("#92fb7b"), 0, 0)
    style.ipt_pm_button.xminimum = 24
    style.ipt_pm_button.align = (0.5, 0.5)

    # 3. Button Text-Style sauber ableiten
    style.ipt_button_text = Style(style.ipt_text)
    style.ipt_button_text.color = "#4f7649"
    style.ipt_button_text.hover_color = "#65b058"
    style.ipt_button_text.insensitive_color = "#888888" # Text deaktiviert (Ausgegraut)
    style.ipt_button_text.xalign = 0.0
    style.ipt_button_text.yalign = 0.5

    style.ipt_center_button_text = Style(style.ipt_text)
    style.ipt_center_button_text.color = "#4f7649"
    style.ipt_center_button_text.hover_color = "#65b058"
    style.ipt_center_button_text.insensitive_color = "#888888" # Text deaktiviert (Ausgegraut)
    style.ipt_center_button_text.xalign = 0.5
    style.ipt_center_button_text.yalign = 0.5

    # 4. Fenster / Dialog-Boxen
    style.ipt_window = Style(style.default) # <- 'style.default' statt 'style.window'!
    style.ipt_window.background = Frame("images/mp.png", 12, 12)
    style.ipt_window.padding = (15, 15, 15, 15)

    # 5. Namensbox für Dialoge
    style.ipt_say_who = Style(style.default)
    style.ipt_say_who.background = Frame("images/mp.png", 40, 40)
    style.ipt_say_who.padding = (15, 15, 15, 15)
    style.ipt_say_who.xminimum = 300
    style.ipt_say_who.yminimum = 50

