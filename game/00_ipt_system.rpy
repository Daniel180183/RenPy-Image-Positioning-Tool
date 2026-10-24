
init offset = 100

define config.quit_action = Quit(confirm=True)

default ipt_show_hidden_button = True

init -1 python:

    # -------------------------------------------------------------
    # ISOLIERTE STYLES FÜR DAS TOOL DEFINIEREN (Präfix "ipt_")
    # -------------------------------------------------------------

    # 1. Isolierter Text-Style
    style.ipt_text = Style(style.default)
    style.ipt_text.font = "DejaVuSansMono.ttf"
    style.ipt_text.size = 14
    style.ipt_text.color = "#000000"
    style.ipt_text.outlines = [] # Verhindert, dass Text-Outlines geerbt werden
    style.ipt_text.line_leading = 0
    style.ipt_text.line_spacing = 0

    # NEU: Verhindert doppelte Zeilenabstände aus Fremdprojekten
    style.ipt_text.line_spacing = 0
    style.ipt_text.line_leading = 0
    style.ipt_text.outlines = []
    style.ipt_text.yfit = True

    # 2. Button-Style komplett isolieren (Kein Erben von style.button)

    # style.ipt_button = Style(style.default) # <- 'style.default' statt 'style.button'!

    style.ipt_button = Style(style.default)
    style.ipt_button.background = Frame(Solid("#84ec6e"), 0, 0)
    style.ipt_button.hover_background = Frame(Solid("#92fb7b"), 0, 0)
    style.ipt_button.padding = (4, 1, 4, 1)
    style.ipt_button.margin = (0, 0, 0, 0)     # Kein ungewolltes Margin aus der gui.rpy erben
    style.ipt_button.xmaximum = 900
    style.ipt_button.yminimum = 0
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

    # NEU: Auch hier Zeilenabstand erzwingen
    style.ipt_button_text.line_spacing = 0
    style.ipt_button_text.line_leading = 0

    style.ipt_center_button_text = Style(style.ipt_text)
    style.ipt_center_button_text.color = "#4f7649"
    style.ipt_center_button_text.hover_color = "#65b058"
    style.ipt_center_button_text.insensitive_color = "#888888" # Text deaktiviert (Ausgegraut)
    style.ipt_center_button_text.xalign = 0.5
    style.ipt_center_button_text.yalign = 0.5

    # 4. Input-Field Style isolieren
    style.ipt_input = Style(style.input)
    style.ipt_input.color = "#84ec6e"
    style.ipt_input.font = "DejaVuSansMono.ttf"
    style.ipt_input.size = 14

    # NEU: Auch für das Eingabefeld fixieren
    style.ipt_input.line_spacing = 0
    style.ipt_input.line_leading = 0

