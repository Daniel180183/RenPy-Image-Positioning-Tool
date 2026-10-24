

###############################################
# Vorhersage ladbare Bilder über RAM und VRAM #
###############################################


default image_width = 1920
default image_height = 1080
default image_bytes_pixel = 4
default layers_max = 0
default layers_max_ram = 0
default layers_max_vram = 0
default test_image_number = 0
default stop_loading_layers = False


init python:
    import psutil
    import subprocess

    def nvidia_vram_free_mb():
        try:
            out = subprocess.check_output(
                ["nvidia-smi",
                 "--query-gpu=memory.free",
                 "--format=csv,noheader,nounits"],
                stderr=subprocess.STDOUT
            ).decode("utf-8", errors="ignore").strip()

            total_vram = 0

            for line in out.splitlines():
                line = line.strip()
                if line:
                    total_vram += int(float(line))

            return total_vram

        except Exception:
            return None

    def update_layers_max():
        # RAM
        ram = psutil.virtual_memory()
        ram_mb = int(ram.available / (1000 * 1000))
        ram_halved = int(ram_mb / 2)

        # VRAM
        vram_free_mb = nvidia_vram_free_mb()

        if vram_free_mb is None:
            vram_free_mb = 2000

        vram_halved = int(vram_free_mb / 2)

        # Speicherbedarf eines Bildes
        image_mb = (
            store.image_width *
            store.image_height *
            store.image_bytes_pixel
        ) / (1000 * 1000)

        # Maximale Layer anhand RAM/VRAM
        store.layers_max_ram = int(ram_halved / image_mb)
        store.layers_max_vram = int(vram_halved / image_mb)

        # Der kleinere Wert ist entscheidend
        store.layers_max = min(store.layers_max_ram,
                               store.layers_max_vram)


#############################
# Bildinformationen abrufen #
#############################


init python:
    import struct
    import os

    def get_image_info(current_directory):

        with open(current_directory, "rb") as f:

            # PNG-Signatur prüfen
            if f.read(8) != b"\x89PNG\r\n\x1a\n":
                return None

            # IHDR-Chunk
            f.read(4)

            if f.read(4) != b"IHDR":
                return None

            width, height, bit_depth, color_type, _, _, _ = \
                struct.unpack(">IIBBBBB", f.read(13))

            channels = {
                0: 1,  # Gray
                2: 3,  # RGB
                3: 1,  # Palette
                4: 2,  # Gray + Alpha
                6: 4,  # RGBA
            }.get(color_type)

            if channels is None:
                return None

            bpp = (bit_depth * channels) / 8.0

            return {
                "width": width,
                "height": height,
                "bpp": bpp,
            }


####################################
# Layer(s) laden und positionieren #
####################################


define config.rollback_enabled = False

define UI_REFERENCE_WIDTH = 1000
define UI_REFERENCE_HEIGHT = 720
define UI_REFERENCE_SCALE_OFFSET = 0.95
define MOVE_REFERENCE_TIME_X = 0.5
define MOVE_REFERENCE_TIME_Y = 0.6
define SCREEN_ABOVE_FOV = -6.0
define UI_REFERENCE_MENU_HEIGHT = (-((SCREEN_ABOVE_FOV) * UI_REFERENCE_HEIGHT)
                                   / (1 - (SCREEN_ABOVE_FOV)))

init python:

    ##################
    # Menüskalierung #
    ##################

    if (not hasattr(persistent, "scale_offset")
        or persistent.scale_offset is None):
        persistent.scale_offset = 0.00


    # Berechnet den Skalierungsfaktor in Abhängigkeit der Projektauflösung.
    def get_ui_scale():
        return min(
            config.screen_width / UI_REFERENCE_WIDTH,
            config.screen_height / UI_REFERENCE_HEIGHT
        ) * (UI_REFERENCE_SCALE_OFFSET - persistent.scale_offset)


    def get_image_move_frame_size():

        frame = renpy.get_widget(
            "image_move",
            "image_move_scaled_frame"
            )

        if frame is None:
            return 0, 0

        render = renpy.render(
            frame,
            config.screen_width,
            config.screen_height,
            0.0,
            0.0
            )

        return render.width, render.height


    def resize_image_move(scale_factor):
        old_scale_offset = persistent.scale_offset
        old_scale = round(get_ui_scale(), 2)

        new_scale_offset = round(old_scale_offset - scale_factor, 2)
        persistent.scale_offset = new_scale_offset

        new_scale = round(get_ui_scale(), 2)

        menu_height = get_image_move_frame_size()[1]
        available_height = config.screen_height - 2

        new_menu_height = (menu_height * new_scale)

        print("resize_image_move")
        print("old_scale_offset:", old_scale_offset)
        print("old_scale:", old_scale)
        print("new_scale_offset:", new_scale_offset)
        print("new_scale:", new_scale)
        print("old menu_height:", menu_height)
        print("new menu_height:", new_menu_height)
        print("available_height:", available_height)
        print("_____________________________________")
        print(" ")

        if new_menu_height > available_height:
            if (show_input_frame
                or image_loading_error
                or delete_query
                or delete_query_data_pos_file
                or show_stop_message
                or show_invalid_float_message
                or show_current_image_parameters):
                persistent.scale_offset = 0.00

            else:
                persistent.scale_offset = old_scale_offset


    # Bewegungszeit horizontal
    def get_move_duration_x():
        scale = get_ui_scale()

        reference_distance = config.screen_width - UI_REFERENCE_WIDTH

        current_distance = config.screen_width - (UI_REFERENCE_WIDTH * scale)

        if reference_distance <= 0:
            return MOVE_REFERENCE_TIME_X

        else:
            return MOVE_REFERENCE_TIME_X * (current_distance / reference_distance)


    # Bewegungszeit vertikal
    def get_move_duration_y():
        scale = get_ui_scale()
        menu_height = get_image_move_frame_size()[1]

        reference_distance = float(config.screen_height - UI_REFERENCE_HEIGHT)

        current_distance = config.screen_height - (UI_REFERENCE_HEIGHT * scale)

        if reference_distance <= 0:
            if menu_height <= 0:
                pass
                return menu_height

            # return (MOVE_REFERENCE_TIME_Y / UI_REFERENCE_HEIGHT) * (menu_height * scale)

            #return MOVE_REFERENCE_TIME_Y * (UI_REFERENCE_HEIGHT / (menu_height * scale))

        # else:
        #     return MOVE_REFERENCE_TIME_Y * (current_distance / reference_distance)


    # Länge Bewegungsstrecke vertikal, Start image_move
    def get_move_yoffset():
        scale = get_ui_scale()
        menu_height = get_image_move_frame_size()[1] * scale
        available_height = config.screen_height

        if menu_height <= 0:
            return available_height

        if menu_height > available_height:
            return available_height

        return min(menu_height, available_height)


    def load_move_values():
        global move_yoffset
        move_yoffset = get_move_yoffset()


        #global move_duration_y
        #move_duration_y = get_move_duration_y()


transform move_down():
    yoffset -move_yoffset
    ease 0.5 yoffset 0


transform move_up():
    yoffset 0
    ease 0.5 yoffset -move_yoffset

transform move_to_right:
    xalign 0.0
    ease 0.5 xalign 1.0


transform move_to_left:
    xalign 1.0
    ease 0.5 xalign 0.0


    # def get_scale_button_center(button_id):
    #
    #     # Ermittelt das Zentrum eines der beiden Skalierungsbuttons
    #     # in Bildschirmkoordinaten.
    #
    #     button = renpy.get_widget(
    #         "image_move",
    #         button_id
    #         )
    #
    #     if button is None:
    #         return None
    #
    #     render = renpy.render(
    #         button,
    #         config.screen_width,
    #         config.screen_height,
    #         0.0,
    #         0.0
    #         )
    #
    #     # Das Renderobjekt selbst kennt seine lokale Größe.
    #     width = render.width
    #     height = render.height
    #
    #     placement = button.get_placement()
    #
    #     xpos = placement[0]
    #     ypos = placement[1]
    #     xanchor = placement[2]
    #     yanchor = placement[3]
    #     xoffset = placement[4]
    #     yoffset = placement[5]
    #
    #     render = renpy.render(
    #         anchor,
    #         config.screen_width,
    #         config.screen_height,
    #         0.0,
    #         0.0
    #
    #     placement = anchor.get_placement()
    #
    #     xpos = placement[0]
    #     ypos = placement[1]
    #     xanchor = placement[2]
    #     yanchor = placement[3]
    #     xoffset = placement[4]
    #     yoffset = placement[5]



# Erkenntnisse:

# -> Warum gelingt ein Aufruf ohne Attribute? - ATL Funktionen in transform haben eine spezielle Schnittstelle und füllen die drei Argumente selbst aus.

# -> Gelingt ein Funktionsaufruf einer Funktion die Argumente erwartet auch ohne Argumente? - Nein, das Argument ist ein Pflichtargument, außer wenn das Argument einen Standardwert hat (def rounds(round_one = 0))

# -> Was wird bei renpy.restart_interaction neu initialisiert? - Der Screen wird neu aufgebaut.

# -> Was geschieht bei return 0.01? Bei einer ATL-Funktion ist dies eine Zeitangabe, welche die Funktion alle 0.01 Sekunden neu aufruft. Abbruch des Neuaufrufes nur über eine Bedingnung in der Funktion. Diese Art von Funktion ist für Transform-Aktualisierungen in Ren'Py gedacht.

    # Skalierung für ein einzeles Elemet was sich bspw. anders als die übrigen verhalten soll.
    # def px(value):
    #     return round(value * ui_scale())

default ipt_font = "DejaVuSansMono.ttf"
default image_move_active = False
default file_location = ""
default layer = -1
default move_layers_simultan = False
default selected_layer = -1
default menu_extension = False
default text_show_var_scams = False
default rotate_range = 1
default zoom_range = 0.01
default xalign_range = 0.01
default yalign_range = 0.01
default zoom_var = 1.0
default xzoom_var = 1.0
default yzoom_var = 1.0
default xalign_var = 0.50
default yalign_var = 0.50
default rotate_var = 0
default h_flip = False
default v_flip = False
default show_saving = False
default current_directory = ""
default file_path = ""
default show_deleting = False
default value_progress_bar = 0
default progress_bar = 0
default total = 0
default image_width_entered = False
default image_height_entered = False
default image_by_pi_entered = False
default slide_image_move_menu_right = False
default image_move_menu_startet = False
default move_into_screen = False
default reload_image_move = False
default keep_image_move = False
default show_stop_message = False
default variable_monitoring_startet = True
default show_image_loading_error = False
default show_message_delete_layers = False
default persistent.data_position_file = False
default message = ""
default error_found = False
default data_project_file = False
default delete_mode = ""
default location_input = "images/"
default display_location_input = "images/"
default show_input_frame = False
default show_file_input = False
default number_input = ""
default show_rotate_input = False
default show_zoom_input = False
default show_xalign_input = False
default show_yalign_input = False
default float_input = ""
default float_value = 0.01
default show_invalid_float_message = False
default image_loading_error = False
default delete_query = False
default delete_query_data_pos_file = False
default show_current_image_parameters = False


default hide_current_menu = False

default move_yoffset = 0.0

default move_duration_y = 0.0


default current_line = ""
default test_line = ""

default cursor_position = 0

default cursor_visible = True
default cursor_blink_start = 0.0

default px_before_cursor = 0
default last_location_input = "images/"

default cursor_lines = []
default last_text_cursor_lines = ""

default test_var = False


# transform move_to_right:
#     xalign 0.0
#     ease get_move_duration_x() xalign 1.0
#
#
# transform move_to_left:
#     xalign 1.0
#     ease get_move_duration_x() xalign 0.0


# transform move_down:
#     yalign get_move_yalign()
#     ease get_move_duration_y() yalign 0.0
#
#
# transform move_up:
#     yalign 0.0
#     ease get_move_duration_y() yalign get_move_yalign()


transform scale_ui(scale):
    zoom scale


transform rotate_label_90_left:
    rotate 270


###################
# Debugging start #
###################

default current_layer = None

screen variable_monitoring():
    $ frame_width, frame_height = get_image_move_frame_size()

    frame:
        if variable_monitoring_startet:
            xalign 1.0
            yalign 0.1

        if slide_image_move_menu_right:
            at move_to_left
            yalign 0.1

        if (not slide_image_move_menu_right
            and not variable_monitoring_startet):
            at move_to_right
            yalign 0.1

        background Frame(Solid("#6db45d"), 6, 6, 6, 6)
        vbox:
            textbutton "get_ui_scale" action [
                Function(get_ui_scale_print)
            ] text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            textbutton "get_image_move_frame_size" action [
                Function(get_image_move_frame_size_print)
                ] text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            textbutton "get_move_duration_x" action [
                Function(get_move_duration_x_print)
                ] text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            textbutton "get_move_duration_y" action [
                Function(get_move_duration_y_print)
                ] text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            label "slide_image_move_menu_right: [slide_image_move_menu_right]" text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            label "keep_image_move: [keep_image_move]" text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            label "image_move_menu_startet: [image_move_menu_startet]" text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

            label "test_var: [test_var]" text_font ipt_font text_size 12 xmaximum 300 xfill True yoffset 2

init python:
    def get_ui_scale_print():
        print("get_ui_scale return:", get_ui_scale())

    def get_image_move_frame_size_print():
        print("get_image_move_frame_size:", get_image_move_frame_size())

    def get_move_duration_x_print():
        print("get_move_duration_x:", get_move_duration_x())

    def get_move_duration_y_print():
        print("get_move_duration_y:", get_move_duration_y())

#{color=#000000}\
#= {color=#ac1111}[]\n\

# Für eine Zeilenüberwachung innerhalb eines "screen":
#   text "Überwachungsname"


# ============================================================
# MINI DEBUG CONSOLE
# Ren'Py 8.3.8
#
# Shift+F1 = Mini-Konsole ein-/ausblenden
#
# Funktionen:
#   - Python-Eingabe
#   - print()-Ausgaben
#   - clear
#   - History mit ↑ / ↓
#   - Interaktiv / Durchlässig
#   - normales Spiel bleibt sichtbar
# ============================================================


# ============================================================
# VARIABLEN
# ============================================================

default mini_console_open = False
default mini_console_input = ""
default mini_console_output = []
default mini_console_history = []
default mini_console_history_position = -1
default mini_console_yadjustment = ui.adjustment(
    ranged=mini_console_scroll_to_bottom
    )
default console_frame_height = 0.28
default console_text_height = 0.18
default plus_button_console_height_held = False
default plus_button_console_height_held_hovered = False
default minus_button_console_height_held = False
default minus_button_console_height_held_hovered = False
default alpha_console = 231
default plus_button_console_bg_alpha = False
default plus_button_console_bg_alpha_hovered = False
default minus_button_console_bg_alpha = False
default minus_button_console_bg_alpha_hovered = False

# True  = Konsole nimmt Maus/Tastaturinteraktion entgegen
# False = Konsole ist nur sichtbar
default mini_console_interactive = True


# ============================================================
# STDOUT -> MINI-KONSOLE
# ============================================================

init python:
    def mini_console_scroll_to_bottom(adjustment):
        adjustment.value = adjustment.range

    def mini_console_stdout(line):

        if not line:
            return

        # Ausgabe übernehmen.
        store.mini_console_output.append(
            str(line)
        )

        # Maximal 200 Zeilen behalten.
        store.mini_console_output = \
            store.mini_console_output[-200:]

        # Screen aktualisieren.
        renpy.restart_interaction()

        # Beim nächsten Layout ans Ende der Ausgabe springen.
        store.mini_console_yadjustment.value = \
            store.mini_console_yadjustment.range


    # Nur einmal registrieren.
    if mini_console_stdout not in config.stdout_callbacks:

        config.stdout_callbacks.append(
            mini_console_stdout
        )


# ============================================================
# OPTIONAL: STDERR -> MINI-KONSOLE
#
# Dadurch können auch Fehlerausgaben angezeigt werden.
# ============================================================

    def mini_console_stderr(line):

        if not line:
            return

        store.mini_console_output.append(
            "[stderr] " + str(line)
        )

        store.mini_console_output = \
            store.mini_console_output[-200:]

        renpy.restart_interaction()

        # Beim nächsten Layout ans Ende der Ausgabe springen.
        store.mini_console_yadjustment.value = \
            store.mini_console_yadjustment.range


    if mini_console_stderr not in config.stderr_callbacks:

        config.stderr_callbacks.append(
            mini_console_stderr
        )


# ============================================================
# PYTHON-BEFEHL AUSFÜHREN
# ============================================================

init python:

    def mini_console_execute(command):

        command = command.strip()

        if not command:
            return


        # ----------------------------------------------------
        # History speichern
        # ----------------------------------------------------

        if (
            not mini_console_history
            or mini_console_history[-1] != command
        ):

            store.mini_console_history.append(
                command
            )


        store.mini_console_history_position = -1


        # ----------------------------------------------------
        # Eingabe anzeigen
        # ----------------------------------------------------

        store.mini_console_output.append(
            "{color=009dd7}>>> " + command
        )


        # ----------------------------------------------------
        # CLEAR
        # ----------------------------------------------------

        if command == "clear":

            store.mini_console_output = []

            renpy.restart_interaction()

            return


        # ----------------------------------------------------
        # PYTHON AUSFÜHREN
        # ----------------------------------------------------

        try:

            # Zuerst versuchen wir einen Ausdruck auszuwerten.

            result = eval(
                command,
                globals(),
                store.__dict__
            )


            if result is not None:

                store.mini_console_output.append(
                    repr(result)
                )

        except SyntaxError:
            # Kein Ausdruck:
            # als Python-Anweisung ausführen.
            try:
                exec(
                    command,
                    globals(),
                    store.__dict__
                )

            except Exception as e:
                store.mini_console_output.append(
                    "{}: {}".format(
                        type(e).__name__,
                        e
                    )
                )

        except Exception as e:
            store.mini_console_output.append(
                "{}: {}".format(
                    type(e).__name__,
                    e
                )
            )


        # ----------------------------------------------------
        # Ausgabe begrenzen
        # ----------------------------------------------------

        store.mini_console_output = \
            store.mini_console_output[-200:]


        renpy.restart_interaction()


# ============================================================
# HISTORY: AUFWÄRTS
# ============================================================

init python:

    def mini_console_history_up():

        if not mini_console_history:
            return


        position = mini_console_history_position


        # Noch keine History-Navigation.
        if position == -1:

            position = len(
                mini_console_history
            ) - 1


        elif position > 0:

            position -= 1


        store.mini_console_history_position = position


        store.mini_console_input = \
            mini_console_history[position]


        renpy.restart_interaction()


# ============================================================
# HISTORY: ABWÄRTS
# ============================================================

    def mini_console_history_down():

        if not mini_console_history:
            return

        position = mini_console_history_position

        if position == -1:
            return

        if position < len(mini_console_history) - 1:
            position += 1

            store.mini_console_history_position = position

            store.mini_console_input = \
                mini_console_history[position]

        else:
            store.mini_console_history_position = -1

            store.mini_console_input = ""

        renpy.restart_interaction()


# ============================================================
# SCREEN
# ============================================================

screen mini_console():
    zorder 1000

    # Shift+F1: Konsole öffnen / schließen
    key "shift_K_F1" action [
        ToggleVariable("mini_console_open")
    ]

    if mini_console_open:
        frame:
            xalign 0.5
            yalign 1.0

            xsize config.screen_width
            ysize int(config.screen_height * console_frame_height)

            background "#101010" + f"{alpha_console:02x}"
            padding (12, 8)

            # Interaktiv  -> True  -> Konsole fängt Mausereignisse ab
            # Durchlässig -> False -> Mausereignisse gehen weiter
            modal mini_console_interactive

            vbox:
                spacing 5

                # -------------------------------------------------
                # Ausgabe
                # -------------------------------------------------

                viewport:
                    ysize int(config.screen_height * console_text_height)

                    yadjustment mini_console_yadjustment

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 1

                        for line in mini_console_output:

                            text line:
                                font ipt_font
                                size 17
                                color "#eeeeee"

                # -------------------------------------------------
                # Eingabe
                # -------------------------------------------------

                hbox:
                    spacing 8

                    text "{color=009dd7}>>>{/color}":
                        font ipt_font
                        size 17
                        yalign 0.5

                    input:

                        value VariableInputValue(
                            "mini_console_input"
                        )

                        action [
                            Function(
                                mini_console_execute,
                                mini_console_input
                            ),
                            SetVariable(
                                "mini_console_input",
                                ""
                            )
                        ]

                        xfill True
                        size 17

                # -------------------------------------------------
                # Buttons
                # -------------------------------------------------

                hbox:
                    spacing 8

                    textbutton "{color=#232629}Clear":
                        action [
                            SetVariable(
                                "mini_console_output",
                                []
                            ),
                            Function(
                                renpy.restart_interaction
                            )
                        ] text_font ipt_font text_size 14

                    hbox:
                        textbutton "{color=#232629}↑":
                            action Function(
                                mini_console_history_up
                            ) text_font ipt_font text_size 14

                        textbutton "{color=#333536}Entered line" text_font ipt_font text_size 14

                        textbutton "{color=#232629}↓":
                            action Function(
                                mini_console_history_down
                            ) text_font ipt_font text_size 14

                    if mini_console_interactive:

                        textbutton "{color=#232629}⊘ Click-through blocked":
                            action [
                                SetVariable("mini_console_interactive", False),
                                SetVariable("alpha_console", 162)
                            ] text_font ipt_font text_size 14

                    else:

                        textbutton "{color=#232629}◉ Click-through console":
                            action [
                                SetVariable("mini_console_interactive", True),
                                SetVariable("alpha_console", 231)
                            ] text_font ipt_font text_size 14

                    textbutton "{color=#232629}Close":
                        action SetVariable(
                            "mini_console_open", False
                        ) text_font ipt_font text_size 14

                    hbox:
                        if console_frame_height < 1.0:
                            textbutton "{color=#333536}+":
                                action SetVariable("plus_button_console_height_held", True)
                                hovered SetVariable("plus_button_console_height_held_hovered", True)
                                unhovered SetVariable("plus_button_console_height_held_hovered", False)
                                text_font ipt_font text_size 14

                            if plus_button_console_height_held_hovered:
                                key "mouseup_1" action SetVariable(
                                    "plus_button_console_height_held", False)

                                key "mousedown_1" action SetVariable(
                                    "plus_button_console_height_held", True)

                            if (plus_button_console_height_held
                                and plus_button_console_height_held_hovered):
                                timer 0.005 repeat True action [
                                    SetVariable("console_frame_height", round(console_frame_height + 0.01, 2)),
                                    SetVariable("console_text_height", round(console_text_height + 0.01, 2))
                                ]

                        else:
                            timer 0.01 action [
                                SetVariable("plus_button_console_height_held", False),
                                SetVariable("plus_button_console_height_held_hovered", False),
                                SetVariable("minus_button_console_height_held", False),
                                SetVariable("minus_button_console_height_held_hovered", False)
                            ]
                            textbutton "{color=#333536}+" text_font ipt_font text_size 14

                        textbutton "{color=#333536}Console height" text_font ipt_font text_size 14

                        if console_frame_height > 0.28:
                            textbutton "{color=#333536}-":
                                action SetVariable("minus_button_console_height_held", True)
                                hovered SetVariable("minus_button_console_height_held_hovered", True)
                                unhovered SetVariable("minus_button_console_height_held_hovered", False)
                                text_font ipt_font text_size 14

                            if minus_button_console_height_held_hovered:
                                key "mouseup_1" action SetVariable(
                                    "minus_button_console_height_held", False)

                                key "mousedown_1" action SetVariable(
                                    "minus_button_console_height_held", True)

                            if (minus_button_console_height_held
                                and minus_button_console_height_held_hovered):
                                timer 0.005 repeat True action [
                                SetVariable("console_frame_height", round(console_frame_height - 0.01, 2)),
                                SetVariable("console_text_height", round(console_text_height - 0.01, 2))
                                ]

                        else:
                            timer 0.01 action [
                                SetVariable("plus_button_console_height_held", False),
                                SetVariable("plus_button_console_height_held_hovered", False),
                                SetVariable("minus_button_console_height_held", False),
                                SetVariable("minus_button_console_height_held_hovered", False)
                            ]

                            textbutton "{color=#333536}-" text_font ipt_font text_size 14

                    hbox:
                        if alpha_console > 9:
                            textbutton "{color=#333536}+":
                                action SetVariable("plus_button_console_bg_alpha", True)
                                hovered SetVariable("plus_button_console_bg_alpha_hovered", True)
                                unhovered SetVariable("plus_button_console_bg_alpha_hovered", False)
                                text_font ipt_font text_size 14

                            if plus_button_console_bg_alpha_hovered:
                                key "mouseup_1" action SetVariable(
                                    "plus_button_console_bg_alpha", False)

                                key "mousedown_1" action SetVariable(
                                    "plus_button_console_bg_alpha", True)

                            if (plus_button_console_bg_alpha
                                and plus_button_console_bg_alpha_hovered):
                                timer 0.005 repeat True action [
                                    SetVariable("alpha_console", alpha_console - 3)
                                ]

                        else:
                            timer 0.05 action [
                                SetVariable("plus_button_console_bg_alpha", False),
                                SetVariable("plus_button_console_bg_alpha_hovered", False),
                                SetVariable("minus_button_console_bg_alpha", False),
                                SetVariable("minus_button_console_bg_alpha_hovered", False)
                            ]

                            textbutton "{color=#333536}+" text_font ipt_font text_size 14

                        textbutton "{color=#333536}Transparency" text_font ipt_font text_size 14

                        if alpha_console < 255:
                            textbutton "{color=#333536}-":
                                action SetVariable("minus_button_console_bg_alpha", True)
                                hovered SetVariable("minus_button_console_bg_alpha_hovered", True)
                                unhovered SetVariable("minus_button_console_bg_alpha_hovered", False)
                                text_font ipt_font text_size 14

                            if minus_button_console_bg_alpha_hovered:
                                key "mouseup_1" action SetVariable(
                                    "minus_button_console_bg_alpha", False)

                                key "mousedown_1" action SetVariable(
                                    "minus_button_console_bg_alpha", True)

                            if (minus_button_console_bg_alpha
                                and minus_button_console_bg_alpha_hovered):
                                timer 0.05 repeat True action [
                                    SetVariable("alpha_console", alpha_console + 3)
                                ]

                        else:
                            timer 0.05 action [
                                SetVariable("plus_button_console_bg_alpha", False),
                                SetVariable("plus_button_console_bg_alpha_hovered", False),
                                SetVariable("minus_button_console_bg_alpha", False),
                                SetVariable("minus_button_console_bg_alpha_hovered", False)
                            ]

                            textbutton "{color=#333536}-" text_font ipt_font text_size 14


# ============================================================
# SCREEN ALS OVERLAY REGISTRIEREN
# ============================================================

init python:

    config.overlay_screens.append(
        "mini_console"
    )


#################
# Debugging end #
#################


screen show_data_pos_file(file_content):
    frame:
        xalign 0.5
        yalign 0.5
        background Frame(Solid("#6db45d"), 6, 6, 6, 6)
        fixed:
            xsize 990
            ysize 720
            viewport:
                xpos 20
                ypos 20
                xsize 950
                ysize 680
                id "show_data_pos_file_viewport"
                mousewheel True
                draggable True

                text file_content:
                    size 16
                    font ipt_font
                    xmaximum 950

            vbar:
                value YScrollValue("show_data_pos_file_viewport")
                xpos 980
                ypos 20
                xsize 8
                ysize 680

                thumb "#4f7649"
                base_bar "#7ede69"

        textbutton "Return" action [
            Show("image_move"),
            Hide("show_data_pos_file", transition = Dissolve(0.2))
        ] xalign 0.98 yalign 0.99 text_font ipt_font text_size 15


screen image_move_hidden():
    zorder 100

    if ipt_show_hidden_button:
        textbutton "{color=#4f7649}Show image move menu{/color}" action [
                Function(save_dev_menu),
                Function(update_layers_max),
                Function(load_move_values),
                Hide("image_move_hidden", transition=Dissolve(0.2)),
                SetVariable("ipt_show_hidden_button", False),
                Show("image_move")
            ] xalign 0.0 yalign 0.0 style "ipt_button" text_style "ipt_button_text" text_size 8

    if ipt_show_hidden_button:
        label "{[project_name_color]}[project_name]   v[project_version]{/color}" xalign 1.0 yalign 1.0 text_size 18

    if ipt_show_hidden_button:
        textbutton "{color=#4f7649}Return to main menu" action [
            MainMenu(confirm = False)
        ] xalign 1.0 yalign 0.0 style "ipt_button" text_style "ipt_button_text" text_size 8


screen return_move_menu():
    zorder 100

    textbutton "{color=#4f7649}Return to image move menu" action [
        SetVariable("hide_current_menu", False),
        Hide("return_move_menu", Dissolve(0.2)),
        Show("image_move")
    ] xalign 0.0 yalign 0.0 style "ipt_button" text_style "ipt_button_text" text_size 8

    label "{[project_name_color]}[project_name]   v[project_version] {/color}"  xalign 1.0 yalign 1.0 text_size 18

    textbutton "{color=#4f7649}Return to main menu" action [
        MainMenu(confirm = False)
    ] xalign 1.0 yalign 0.0 style "ipt_button" text_style "ipt_button_text" text_size 8


screen wait_enter_only():
    timer 0.01 action Function(resize_image_move, 0.00)
    key "K_RETURN" action Return(True)


init python:
    import time

    # Diese Unterklasse erbt von der Basisklasse "VariableInputValue".
    # set_text() ist eine Methode von VariableInputValue.
    # super(FilePathInputValue, self).set_text(text) bedeutet: Führe jetzt die ursprüngliche set_text()-Methode der Elternklasse VariableInputValue aus.
    # VariableInputValue kann also auch direkt verwendet werden.

    # Die ursprüngliche Idee:
        # Aus der Datei "behavior.py"
        # map_event(ev, "input_left") und
        # map_event(ev, "input_right")
        # der Klasse "Input" nutzen, um die Pfeiltasten links und rechts direkt auszulesen.


    # class FilePathInputValue(VariableInputValue):
    #
    #     def set_text(self, text):
    #
    #         # Normales Speichern der Variable
    #         super(FilePathInputValue, self).set_text(text)

    # ____________________________

    # KEINE PROGRAMMFUNKTION!!! Nur zum Testen

    # MyCaret erbt von CaretBlink. Möglicherweise kann ich das Verhalten des Originalcursos auf meinen Cursor anwenden.

    # EventInput: überschneidet sich diese Methode in Ren'Py?

    # class MyCaret(CaretBlink):
    #
    #     def __init__(self, caret, caret_blink, **properties):
    #         super(MyCaret, self).__init__(
    #             caret,
    #             caret_blink,
    #             **properties
    #             )


    def get_display_text():
        text = location_input

        result = ""
        current_line = ""

        for char in text:

            test_line = current_line + char

            displayed_text = Text(
                test_line,
                text_size = 16,
                text_font = ipt_font
            )

            rendered_text = renpy.render(
                displayed_text,
                10000,
                10000,
                0,
                0
            )

            if rendered_text.width <= 553:
                current_line = test_line

            else:
                result += current_line + "\n"
                current_line = char

        result += current_line

        #print(current_line)
        #print(result)

        return result

    # Funktionierende Variante für x-Verschiebung.

    # def update_location_cursor():
    #     global cursor_position
    #     global px_before_cursor
    #     global last_location_input
    #     cursor_px_offset_left = 3
    #
    #     widget = renpy.get_widget("image_move", "location_input")
    #
    #     if widget is not None:
    #         new_position = widget.caret_pos
    #
    #         if (new_position != cursor_position
    #             or location_input != last_location_input):
    #             reset_cursor_blink()
    #
    #     if (new_position == cursor_position
    #         and location_input == last_location_input):
    #         return
    #
    #     cursor_position = new_position
    #     last_location_input = location_input
    #
    #     displayed_text = Text(location_input[:cursor_position], size = 16)
    #     rendered_text = renpy.render(displayed_text, 10000, 100, 0, 0)
    #
    #     px_before_cursor = round(rendered_text.width) - cursor_px_offset_left


    def update_location_cursor():
        global cursor_position
        global px_before_cursor
        global last_location_input

        cursor_px_offset_left = 3

        widget = renpy.get_widget("image_move", "location_input")

        if widget is None:
            return

        new_position = widget.caret_pos

        position_changed = new_position != cursor_position
        text_changed = location_input != last_location_input

        if not position_changed and not text_changed:
            return

        if position_changed or text_changed:
            reset_cursor_blink()

        # Neue Cursorposition übernehmen
        cursor_position = new_position

        # Jetzt kennt update_cursor_lines() die neue Position
        if position_changed:
            update_cursor_lines()

        last_location_input = location_input

        displayed_text = Text(
            location_input[:cursor_position],
            size = 16,
            font = ipt_font
        )

        rendered_text = renpy.render(
            displayed_text, 10000, 100, 0, 0)

        px_before_cursor = round(rendered_text.width) - cursor_px_offset_left


    def update_cursor_blink():
        global cursor_visible
        global cursor_blink_start

        # Zeit seit dem letzten Reset des Blinkzyklus.
        elapsed = time.time() - cursor_blink_start

        # Nach 0,6 Sekunden Sichtbarkeit wechseln.
        if elapsed >= 0.6:
            cursor_visible = not cursor_visible

            cursor_blink_start = time.time()


    def reset_cursor_blink():
        global cursor_visible
        global cursor_blink_start

        cursor_visible = True
        cursor_blink_start = time.time()


    def get_cursor_lines():

        text = location_input

        lines = []
        current_line = ""
        line_start = 0

        for i, char in enumerate(text):

            test_line = current_line + char

            displayed_text = Text(test_line, style = "input_text")
            rendered_text = renpy.render(displayed_text, 10000, 10000, 0, 0)

            if rendered_text.width <= 553:
                current_line = test_line

            else:
                lines.append({
                    "text": current_line,
                    "start": line_start,
                    "end": i
                })

                current_line = char
                line_start = i

        # Letzte Zeile hinzufügen.
        lines.append({
            "text": current_line,
            "start": line_start,
            "end": len(text)
        })

        return lines


    def move_cursor_vertical(direction):

        widget = renpy.get_widget("image_move", "location_input")

        if widget is None:
            return

        lines = get_cursor_lines()

        # Aktuelle Zeile finden.
        current_line_number = None

        for line_number, line in enumerate(lines):

            if line["start"] <= cursor_position < line["end"]:
                current_line_number = line_number
                break

        # Cursor am Ende des gesamten Textes.
        if cursor_position == len(location_input):
            current_line_number = len(lines) - 1

        if current_line_number is None:
            return

        # Zielzeile bestimmen.
        target_line_number = current_line_number + direction

        # Oberhalb der ersten bzw. unterhalb der letzten Zeile
        # gibt es nichts mehr zu tun.
        if target_line_number < 0:
            return

        if target_line_number >= len(lines):
            return

        current_line = lines[current_line_number]
        target_line = lines[target_line_number]

        # Cursorposition innerhalb der aktuellen Zeile.
        relative_position = cursor_position - current_line["start"]

        # Zielposition zunächst auf dieselbe Zeichenposition setzen.
        target_position = target_line["start"] + relative_position

        # Nicht hinter das Ende der Zielzeile gehen.
        if target_position > target_line["end"]:
            target_position = target_line["end"]

        # Cursor des echten Ren'Py-Inputs bewegen.
        widget.caret_pos = target_position

        # Blinkzyklus zurücksetzen.
        global cursor_visible
        global cursor_blink_start

        cursor_visible = True
        cursor_blink_start = time.time()


    def get_cursor_line_info():

        for line_number, line in enumerate(cursor_lines):

            if line["start"] <= cursor_position < line["end"]:

                relative_position = cursor_position - line["start"]

                return line_number, relative_position

        # Sicherheitsfall: keine Zeilen vorhanden.
        if not cursor_lines:
            return 0, 0

        # Sicherheitsfall: Cursor am Ende des Textes.
        last_line = len(cursor_lines) - 1
        relative_position = cursor_position - cursor_lines[last_line]["start"]

        return last_line, relative_position


    def update_cursor_lines():
        global cursor_lines
        global last_text_cursor_lines

        if location_input == last_text_cursor_lines:
            return

        cursor_lines = get_cursor_lines()
        last_text_cursor_lines = location_input


screen image_move_restart():
    timer 0.01 action [
        Hide("image_move"),
        Show("image_move")
    ]


screen image_move():

    timer 0.01 action [
        Hide("image_move_restart"),
    ]

    if not reload_image_move:
        on "show" action [
                SetVariable("image_move_menu_startet", True),
                SetVariable("move_into_screen", True)
            ]

    if not move_into_screen:
        timer 0.5 action [
            SetVariable("image_move_menu_startet", False),
            SetVariable("reload_image_move", False),
            Hide("image_move"),
            Show("image_move_hidden", Dissolve(0.2)),
            SetVariable("slide_image_move_menu_right", False)
        ]

    if hide_current_menu:
        timer 0.5 action [
            Hide("image_move"),
            Show("return_move_menu", Dissolve(0.2))
        ]

    frame:
        background Solid("#2e4a2a")
        padding(4, 2)

        if reload_image_move:
            yalign 0.0

        # if image_move_menu_startet:
        #     xalign 0.0

        if (slide_image_move_menu_right):
            at move_to_right
            yalign 0.0

        if (not slide_image_move_menu_right):
            at move_to_right
            yalign 0.0

        # if slide_image_move_menu_right:
        #     at move_to_left
        #     yalign 0.1
        #
        # if (not slide_image_move_menu_right
        #     and not variable_monitoring_startet):
        #     at move_to_right
        #     yalign 0.1

        if (move_into_screen
            and not reload_image_move):
            at move_down

        if (not move_into_screen or
            hide_current_menu):
            if not slide_image_move_menu_right:
                xalign 0.0

            if slide_image_move_menu_right:
                xalign 1.0

            at move_up
        #
        # if (slide_image_move_menu_right
        #     and keep_image_move):
        #     xalign 1.0
        #
        # if (not slide_image_move_menu_right
        #     and keep_image_move):
        #     xalign 0.0

        frame:
            id "image_move_scaled_frame"

            at scale_ui(get_ui_scale())

            vbox:
                hbox:
                    vbox:
                        hbox:
                            vbox:
                                if (layer != -1
                                    and not show_input_frame
                                    and not image_loading_error
                                    and not delete_query
                                    and not delete_query_data_pos_file
                                    and not show_stop_message
                                    and not show_current_image_parameters):

                                    null height 2

                                    textbutton "Rotate left ( {b}[rotate_var]{/b} )" action [
                                        SetVariable("rotate_var", rotate_var - rotate_range),
                                        Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Rotate right ( {b}[rotate_var]{/b} )" action [
                                        SetVariable("rotate_var", rotate_var + rotate_range),
                                        Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    if (not show_input_frame
                                        and not image_loading_error
                                        and not delete_query
                                        and not delete_query_data_pos_file
                                        and not show_stop_message
                                        and not show_current_image_parameters):
                                        textbutton "Zoom +   ( {b}[zoom_var:.2f]{/b} )" action [
                                            SetVariable("zoom_var", zoom_var + zoom_range),
                                            Jump("restart_image")
                                        ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                        null height 2

                                    if (show_input_frame
                                        and not image_loading_error
                                        and not delete_query
                                        and not delete_query_data_pos_file
                                        and not show_stop_message
                                        and not show_current_image_parameters):
                                        textbutton "Zoom +   ( {b}[zoom_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                        null height 2

                                    if (not show_input_frame
                                        and not image_loading_error
                                        and not delete_query
                                        and not delete_query_data_pos_file
                                        and not show_stop_message
                                        and not show_current_image_parameters):
                                        textbutton "Zoom -   ( {b}[zoom_var:.2f]{/b} )" action [
                                            SetVariable("zoom_var", zoom_var - zoom_range), Jump("restart_image")
                                        ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                        null height 2

                                    if (show_input_frame
                                        and not image_loading_error
                                        and not delete_query
                                        and not delete_query_data_pos_file
                                        and not show_stop_message
                                        and not show_current_image_parameters):
                                        textbutton "Zoom -   ( {b}[zoom_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                        null height 2

                                    textbutton "Xalign +   ( {b}[xalign_var:.2f]{/b} )" action [
                                        SetVariable("xalign_var", xalign_var + xalign_range),
                                        Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Xalign -   ( {b}[xalign_var:.2f]{/b} )" action [
                                        SetVariable("xalign_var", xalign_var - xalign_range),
                                        Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Yalign +   ( {b}[yalign_var:.2f]{/b} )" action [ SetVariable("yalign_var", yalign_var + yalign_range), Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Yalign -   ( {b}[yalign_var:.2f]{/b} )" action [
                                        SetVariable("yalign_var", yalign_var - yalign_range), Jump("restart_image")
                                    ] style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                if (layer == -1
                                    or show_input_frame
                                    or image_loading_error
                                    or delete_query
                                    or delete_query_data_pos_file
                                    or show_stop_message
                                    or show_current_image_parameters):

                                    null height 2

                                    textbutton "Rotate left ( {b}[rotate_var]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Rotate right ( {b}[rotate_var]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Zoom +   ( {b}[zoom_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Zoom -   ( {b}[zoom_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Xalign +   ( {b}[xalign_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Xalign -   ( {b}[xalign_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Yalign +   ( {b}[yalign_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                                    null height 2

                                    textbutton "Yalign -   ( {b}[yalign_var:.2f]{/b} )" style "ipt_button" text_style "ipt_button_text" xsize 224 ysize 22

                            vbox:

                                hbox:
                                    null width 2

                                    vbox:
                                        if (not show_input_frame
                                            and not image_loading_error
                                            and not delete_query
                                            and not delete_query_data_pos_file
                                            and not show_stop_message
                                            and not show_current_image_parameters):

                                            null height 2

                                            textbutton " + " action [
                                                SetVariable("rotate_range", rotate_range + 1)
                                            ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " action [
                                                SetVariable("zoom_range", zoom_range + 0.01)
                                            ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " action [
                                                SetVariable("xalign_range", xalign_range + 0.01)
                                            ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " action [
                                                SetVariable("yalign_range", yalign_range + 0.01)
                                            ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                        if (show_input_frame
                                            or image_loading_error
                                            or delete_query
                                            or delete_query_data_pos_file
                                            or show_stop_message
                                            or show_current_image_parameters):

                                            null height 2

                                            textbutton " + " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " + " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                    null width 2

                                    vbox:
                                        null height 2
                                        if (not show_input_frame
                                            and not image_loading_error
                                            and not delete_query
                                            and not delete_query_data_pos_file
                                            and not show_stop_message
                                            and not show_current_image_parameters):

                                            textbutton " Rotate range: {b}[rotate_range]{/b}" action [
                                                Jump("input_rotate")
                                            ] style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Zoom range: {b}[zoom_range:.2f]{/b}" action [
                                                Jump("input_zoom")
                                            ] style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Xalign range: {b}[xalign_range:.2f]{/b}" action [
                                                Jump("input_xalign")
                                            ] style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Yalign range: {b}[yalign_range:.2f]{/b}" action [
                                                Jump("input_yalign")
                                            ] style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                        else:
                                            textbutton " Rotate range: {b}[rotate_range]{/b}" style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Zoom range: {b}[zoom_range:.2f]{/b}" style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Xalign range: {b}[xalign_range:.2f]{/b}" style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                            textbutton " Yalign range: {b}[yalign_range:.2f]{/b}" style "ipt_button" text_style "ipt_button_text" xsize 144 ysize 40

                                            null height 2

                                    null width 2
                                    vbox:

                                        null height 2

                                        if (not show_input_frame
                                            and not image_loading_error
                                            and not delete_query
                                            and not delete_query_data_pos_file
                                            and not show_stop_message
                                            and not show_current_image_parameters):
                                            textbutton " - " action [
                                                    SetVariable("rotate_range", rotate_range - 1), Jump("image_loop")
                                                ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " action [
                                                    SetVariable("zoom_range", zoom_range - 0.01),
                                                    Jump("image_loop")
                                                ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " action [
                                                    SetVariable("xalign_range", xalign_range - 0.01), Jump("image_loop")
                                                ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " action [
                                                    SetVariable("yalign_range", yalign_range - 0.01), Jump("image_loop")
                                                ] style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                        if (show_input_frame
                                            or image_loading_error
                                            or delete_query
                                            or delete_query_data_pos_file
                                            or show_stop_message
                                            or show_current_image_parameters):

                                            textbutton " - " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                            null height 2

                                            textbutton " - " style "ipt_pm_button" text_style "ipt_button_text" xsize 24 ysize 40

                                hbox:
                                    null height 2
                                    null width 2

                                    if (layer != -1
                                        and not show_input_frame
                                        and not image_loading_error
                                        and not delete_query
                                        and not delete_query_data_pos_file
                                        and not show_stop_message
                                        and not show_current_image_parameters):
                                        python:
                                            current_layer = get_selected_layer()

                                        if current_layer != -1:
                                            if h_flip:
                                                textbutton "{color=#cb1e1e}Flip h" action [
                                                    SetVariable("h_flip", False),
                                                    SetVariable("keep_image_move", True),
                                                    Jump("restart_image")
                                                ] style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                                            else:
                                                textbutton "{color=#4f7649}Flip h" action [
                                                    SetVariable("h_flip", True),
                                                    SetVariable("keep_image_move", True),
                                                    Jump("restart_image")
                                                ] style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                                        null width 2

                                        if current_layer != -1:
                                            if v_flip:
                                                textbutton "{color=#cb1e1e}Flip v" action [
                                                    SetVariable("v_flip", False),
                                                    SetVariable("keep_image_move", True),
                                                    Jump("restart_image")
                                                ] style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                                            else:
                                                textbutton "{color=#4f7649}Flip v" action [
                                                    SetVariable("v_flip", True),
                                                    SetVariable("keep_image_move", True),
                                                    Jump("restart_image")
                                                ] style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                                    else:

                                        textbutton "Flip h" style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                                        null width 2

                                        textbutton "Flip v" style "ipt_button" text_style "ipt_button_text" xsize 97 ysize 22 text_size 14

                        null height 2

                        textbutton "{color=0a2bb5}Estimated maximum number of layers: [layers_max]" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        hbox:
                            if (not show_input_frame
                                and not show_stop_message
                                and not image_loading_error
                                and not delete_query
                                and not delete_query_data_pos_file
                                and not show_stop_message
                                and not show_invalid_float_message
                                and not show_current_image_parameters):
                                textbutton "{color=#4f7649}Image size:\nWidth = [image_width] | Height = [image_height]\nBytes / pixel = [image_bytes_pixel]" action [
                                    SetVariable("keep_image_move", True),
                                    Jump("input_image_size")
                                ] style "ipt_button" text_style "ipt_button_text" xsize 260 ysize 60
                                null width 2

                            if (not show_input_frame
                                and not show_stop_message
                                and not image_loading_error
                                and not delete_query
                                and not delete_query_data_pos_file
                                and not show_stop_message
                                and not show_invalid_float_message
                                and not show_current_image_parameters
                                and not layer == -1):
                                textbutton "{color=#4f7649}Get parameters\nof the last\nloaded image." action [
                                    SetVariable("keep_image_move", True),
                                    Jump("get_image_info")
                                ] style "ipt_button" text_style "ipt_button_text" xsize 160 ysize 60

                            if (show_input_frame
                                or image_loading_error
                                or delete_query
                                or delete_query_data_pos_file
                                or show_stop_message
                                or show_invalid_float_message
                                or show_current_image_parameters):
                                textbutton "{color=#4f7649}Image size:\nWidth = [image_width] | Height = [image_height]\nBytes / pixel = [image_bytes_pixel]" style "ipt_button" text_style "ipt_button_text" xsize 260 ysize 60
                                null width 2

                            if (show_input_frame
                                or image_loading_error
                                or delete_query
                                or delete_query_data_pos_file
                                or show_stop_message
                                or show_invalid_float_message
                                or show_current_image_parameters
                                or layer == -1):
                                textbutton "{color=#4f7649}Get parameters\nof the last\nloaded image." style "ipt_button" text_style "ipt_button_text" xsize 160 ysize 60

                        null height 2

                        textbutton "{color=0a2bb5}Number of active layers: [layer + 1]" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (move_layers_simultan
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Move layers simultaneously: on" action [
                                SetVariable("move_layers_simultan", False),
                                SetVariable("selected_layer", 0)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                            null height 2

                            textbutton "Move layers individually: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (move_layers_simultan
                            and (show_input_frame
                                or image_loading_error
                                or delete_query
                                or delete_query_data_pos_file
                                or show_stop_message
                                or show_invalid_float_message
                                or show_current_image_parameters)):
                                textbutton "{color=#4f7649}Move layers simultaneously: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                                null height 2

                                textbutton "Move layers individually: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (not move_layers_simultan
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "Move layers simultaneously: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                            null height 2

                            textbutton "{color=#4f7649}Move layers individually: on" action [
                                SetVariable("move_layers_simultan", True),
                                Hide("image_loading_error"),
                                SetVariable("image_found", False)
                                ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (not move_layers_simultan
                            and (show_input_frame
                                or image_loading_error
                                or delete_query
                                or delete_query_data_pos_file
                                or show_stop_message
                                or show_invalid_float_message
                                or show_current_image_parameters)):
                                textbutton "Move layers simultaneously: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                                null height 2

                                textbutton "Move layers individually: off" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (layer != -1
                            and not move_layers_simultan
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Selected layer: [selected_layer + 1]" action [
                                Hide("image_loading_error"),
                                SetVariable("image_found", False),
                                Jump("restart_layer_counter")
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (layer != -1
                            and (show_input_frame
                                or image_loading_error
                                or delete_query
                                or delete_query_data_pos_file
                                or show_stop_message
                                or show_invalid_float_message
                                or show_current_image_parameters)):
                                textbutton "Selected layer: [selected_layer + 1]" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if layer == -1:
                            textbutton "No layer loaded" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (layer != -1
                            and move_layers_simultan):
                            textbutton "All layers selected" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (not move_layers_simultan
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Input file location":
                                id "image_move_scale_minus"
                                action [
                                Hide("image_loading_error"),
                                SetVariable("image_move_active", True),
                                SetVariable("image_loading_error", False),
                                SetVariable("keep_image_move", True),
                                Jump("input_image")
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (move_layers_simultan
                            or show_input_frame
                            or image_loading_error
                            or delete_query
                            or delete_query_data_pos_file
                            or show_stop_message
                            or show_invalid_float_message
                            or show_current_image_parameters):
                            textbutton "Input file location" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (layer > -1
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Delete layer(s)" action [
                                SetVariable("delete_mode", "layers"),
                                SetVariable("selected_layer", -1),
                                Hide("image_loading_error"),
                                Hide("message_delete_layers"),
                                SetVariable("delete_query", True),
                                SetVariable("stop_loading_layers", False),
                                SetVariable("keep_image_move", True),
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (layer == -1
                            or show_input_frame
                            or image_loading_error
                            or delete_query
                            or delete_query_data_pos_file
                            or show_stop_message
                            or show_invalid_float_message
                            or show_current_image_parameters):
                            textbutton "Delete layer(s)" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (not show_input_frame
                            and layer > -1
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#cb1e1e}Continue game and delete image(s){/color}" action [
                                SetVariable("keep_image_move", True),
                                SetVariable("delete_mode", "continue"),
                                SetVariable("delete_query", True),
                                SetVariable("ipt_show_hidden_button", True)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (not show_input_frame
                            and layer == -1
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Continue game" action [
                                SetVariable("keep_image_move", True),
                                SetVariable("move_into_screen", False),
                                SetVariable("ipt_show_hidden_button", True),
                                Jump("load_dev_menu_save")
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (show_input_frame
                            or image_loading_error
                            or delete_query
                            or delete_query_data_pos_file
                            or show_stop_message
                            or show_invalid_float_message
                            or show_current_image_parameters):
                            textbutton "Continue game" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (not show_saving
                            and layer > -1
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Save layer data" action [
                                SetVariable("keep_image_move", True),
                                SetVariable("delete_mode", "continue"),
                                SetVariable("show_saving", True),
                                Jump("anim_progress_bar")
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (layer == -1
                            or show_input_frame
                            or image_loading_error
                            or delete_query
                            or delete_query_data_pos_file
                            or show_stop_message
                            or show_invalid_float_message
                            or show_current_image_parameters):
                            textbutton "Save layer data" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (show_saving
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            frame:
                                xalign 0.5
                                yalign 0.5
                                padding (3, 6)
                                fixed:
                                    xsize 408
                                    ysize 11
                                    bar:
                                        value progress_bar
                                        range 100
                                        xsize 408
                                        ysize 11
                                        xalign 0.5
                                        yalign 0.5
                                        left_bar Solid("#cb1e1e")
                                        right_bar Solid("#58934a")
                                        thumb None
                                    text "save position data...":
                                        xalign 0.5
                                        yalign 0.5
                                        size 14
                                        font ipt_font

                        null height 2

                        if (not persistent.data_position_file
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "Delete layer data" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (persistent.data_position_file
                            and not show_deleting
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Delete layer data" action [
                                SetVariable("keep_image_move", True),
                                SetVariable("delete_query_data_pos_file", True)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (show_input_frame
                            or image_loading_error
                            or delete_query
                            or delete_query_data_pos_file
                            or show_stop_message
                            or show_invalid_float_message
                            or show_current_image_parameters):
                            textbutton "Delete layer data" style "ipt_button" text_style "ipt_button_text" xsize 422

                        if (persistent.data_position_file
                            and show_deleting
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            frame:
                                xalign 0.5
                                yalign 0.5
                                padding (3, 6)
                                fixed:
                                    xsize 408
                                    ysize 11
                                    bar:
                                        value progress_bar
                                        range 100
                                        xsize 408
                                        ysize 10
                                        xalign 0.5
                                        yalign 0.5
                                        left_bar Solid("#cb1e1e")
                                        right_bar Solid("#58934a")
                                        thumb None
                                    text "Delete position data...":
                                        xalign 0.5
                                        yalign 0.5
                                        size 14
                                        font ipt_font

                        null height 2

                        if (not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Hide current menu" action [
                                Hide("image_loading_error"),
                                Hide("message_delete_layers"),
                                Hide("locationput"),
                                SetVariable("hide_current_menu", True)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        else:
                            textbutton "Hide current menu" style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if not slide_image_move_menu_right:
                            textbutton "{color=#4f7649}Menu on the right" action [
                                SetVariable("slide_image_move_menu_right", True)#,
                                #SetVariable("keep_image_move", False)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        if slide_image_move_menu_right:
                            textbutton "{color=#4f7649}Menu on the left" action [
                                SetVariable("image_move_menu_startet", False),
                                SetVariable("slide_image_move_menu_right", False),
                                SetVariable("variable_monitoring_startet", False),
                                SetVariable("keep_image_move", False)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        null height 2

                        if (persistent.data_position_file
                            and not show_input_frame
                            and not image_loading_error
                            and not delete_query
                            and not delete_query_data_pos_file
                            and not show_stop_message
                            and not show_invalid_float_message
                            and not show_current_image_parameters):
                            textbutton "{color=#4f7649}Show saved layer data" action [
                                SetVariable("keep_image_move", True),
                                Hide("image_move"),
                                Hide("image_move_hidden"),
                                Jump("show_layer_pos_txt")
                            ] style "ipt_button" text_style "ipt_button_text" xsize 422

                        else:
                            textbutton "{color=#4f7649}Show saved layer data" style "ipt_button" text_style "ipt_button_text" xsize 422

                    null width 2

                    vbox:
                        null height 2

                        textbutton "{color=#4f7649}+":
                            action [
                                Function(resize_image_move, + 0.01)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 20 ysize 111

                        null height 2

                        fixed:
                            xsize 20
                            ysize 299

                            textbutton "{color=#4f7649}Menu Scaling" style "ipt_button" text_style "ipt_center_button_text" xsize 300 ysize 20 at rotate_label_90_left

                        null height 2

                        textbutton "{color=#4f7649}-":
                            action [
                                Function(resize_image_move, - 0.01)
                            ] style "ipt_button" text_style "ipt_button_text" xsize 20 ysize 111

                null height 2

                textbutton "{color=#4f7649}Open/Close Console (SHIFT + F1)" action [
                        ToggleVariable("mini_console_open")
                    ] style "ipt_button" text_style "ipt_button_text" xsize 444

                null height 2

                if show_input_frame:
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        xalign 0.5
                        textbutton "{color=4f7649}Return" action [
                          SetVariable("layers_simultan", False),
                          SetVariable("image_move_active", False),
                          SetVariable("show_input_frame", False),
                          SetVariable("show_file_input", False),
                          SetVariable("show_rotate_input", False),
                          SetVariable("show_zoom_input", False),
                          SetVariable("show_xalign_input", False),
                          SetVariable("show_yalign_input", False),
                          SetVariable("image_width_entered", False),
                          SetVariable("image_height_entered", False),
                          SetVariable("image_by_pi_entered", False),
                          SetVariable("keep_image_move", True),
                          SetVariable("stop_loading_layers", False),
                          SetVariable("show_invalid_float_message", False),
                          SetVariable("show_current_image_parameters", False),
                          Jump("image_loop")
                        ] xalign 1.0 yalign 1.0 text_size 16 style "ipt_text"

                        vbox:
                            if show_file_input:
                                text "{color=4f7649}Please enter the folder path and file name, then press Enter:" size 18 font ipt_font

                            if show_rotate_input:
                                text "{color=4f7649}Please enter the rotate range, then press Enter:" size 18 font ipt_font

                            if image_width_entered:
                                text "{color=4f7649}Please enter the image width, then press Enter:" size 18 font ipt_font

                            if image_height_entered:
                                text "{color=4f7649}Please enter the image height, then press Enter:" size 18 font ipt_font

                            if  image_by_pi_entered:
                                text "{color=4f7649}Please enter the bytes per pixel, then press Enter:" size 18 font ipt_font

                            if show_zoom_input:
                                text "{color=4f7649}Please enter the zoom range, then press Enter:" size 18 font ipt_font

                            if show_xalign_input:
                                text "{color=4f7649}Please enter the xalign range, then press Enter:" size 18 font ipt_font

                            if show_yalign_input:
                                text "{color=4f7649}Please enter the yalign range, then press Enter:" size 18 font ipt_font

                            # Anzeige im Input-Frame mit Cursor
                            if show_file_input:

                                # Alle 0.05 Sekunden den Cursor aktualisieren.
                                timer 0.05 repeat True action [
                                  Function(update_location_cursor),
                                  Function(update_cursor_blink)
                                ]

                                fixed:
                                    # Sichtbare Textdarstellung
                                    text "[get_display_text()]":
                                        size 16
                                        font ipt_font
                                        color "#0a2bb5"
                                        xmaximum 553

                                    # Sichtbare Cursordarstellung
                                    showif cursor_visible:
                                        text "|":
                                            size 16
                                            font ipt_font
                                            color "#0a2bb5"
                                            xpos px_before_cursor
                                            ypos 0

                            input:
                                # Eingabe unverändert speichern (unsichtbar)
                                if show_file_input:
                                    id "location_input"
                                    value VariableInputValue("location_input",
                                                            returnable = True)
                                    xsize 10000
                                    length 170
                                    size 16
                                    font ipt_font
                                    color "#00000000"
                                    multiline True

                                if (show_rotate_input
                                    or image_width_entered
                                    or image_height_entered):
                                        id "number_input"
                                        value VariableInputValue("number_input",
                                                                returnable = True)
                                        allow "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
                                        length 4
                                        size 16
                                        color "#0a2bb5"

                                if image_by_pi_entered:
                                    id "number_input"
                                    value VariableInputValue("number_input",
                                                            returnable = True)
                                    allow "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
                                    length 3
                                    size 16
                                    color "#0a2bb5"

                                if (show_input_frame
                                    and (show_zoom_input
                                        or show_xalign_input
                                        or show_yalign_input)):
                                        id "float_input"
                                        value VariableInputValue("float_input",
                                                                returnable = True)
                                        allow "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ."
                                        length 4
                                        exclude "{}"
                                        size 16
                                        color "#0a2bb5"

                if image_loading_error:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        label "{color=#cb1e1e}{b}Image file not found.{/b}\n\nPlease enter the correct folder path and the file name, including the file extension.\n\nSupported file types: png, jpg, jpeg, webp, avif, svg" text_size 16

                        textbutton "{color=#4f7649}Return" action [
                          SetVariable("image_loading_error", False)
                        ] at right text_size 16

                if delete_query:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        vbox:
                            xalign 0.5
                            ypos 15
                            spacing 10
                            label "{color=#cb1e1e}Are you sure you want to delete all layers?" xalign 0.5 text_size 16

                            hbox:
                                xalign 0.5
                                ypos 40
                                spacing 100

                                if delete_mode == "layers":
                                    textbutton "{color=#cb1e1e}Yes" xsize 50 text_size 16 action [
                                      SetVariable("layers_max", 0),
                                      SetVariable("stop_loading_layers", False),
                                    Jump("delete_layers_only")
                                    ]

                                if delete_mode == "continue":
                                    textbutton "{color=#cb1e1e}Yes" xsize 50 text_size 16 action [
                                        SetVariable("move_into_screen", False),
                                        Jump("delete_image_move")
                                    ]

                                textbutton "{color=#238626}No" xsize 50 text_size 16 action [
                                    SetVariable("delete_query", False),
                                ]

                if delete_query_data_pos_file:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        vbox:
                            xalign 0.5
                            ypos 15
                            spacing 10
                            label "{color=#cb1e1e}Are you sure you want to delete all position data from the file?" xalign 0.5 text_size 16

                            hbox:
                                xalign 0.5
                                ypos 25
                                spacing 100

                                textbutton "{color=#cb1e1e}Yes" xsize 50 text_size 16 action [
                                  SetVariable("delete_query_data_pos_file", False),
                                  SetVariable("show_deleting", True),
                                  Jump("anim_progress_bar")
                                ]

                                textbutton "{color=#238626}No" xsize 50 text_size 16 action [
                                  SetVariable("delete_query_data_pos_file", False),
                                  Jump("image_loop")
                                ]

                if show_stop_message:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        vbox:
                            xalign 0.5
                            ypos 15
                            spacing 10
                            label "{color=#cb1e1e}Maximum number of layers reached." xalign 0.5 text_size 16

                            label "{color=#cb1e1e}Please delete the current layers." xalign 0.5 text_size 16

                        textbutton "Return" action [
                          SetVariable("show_stop_message", False)
                        ] at right text_size 16

                if show_invalid_float_message:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        vbox:
                            xalign 0.5
                            ypos 15
                            label "{color=#cb1e1e}Invalid input." xsize 416 text_size 16

                            label "{color=#cb1e1e}Only values between 0.01 and 1.00 are valid." xsize 416 text_size 16

                        textbutton "Return" action [
                          SetVariable("show_invalid_float_message", False)
                        ] at right text_size 16

                if show_current_image_parameters:
                    timer 0.01 action Function(resize_image_move, 0.00)
                    frame:
                        background Solid("#84ec6e")
                        padding(4, 2, 4, 2)
                        xsize 444
                        ysize 150
                        at center

                        vbox:
                            ypos 15
                            label "{color=0a2bb5}Parameters of the last loaded image:\n" text_size 16

                            label "{color=0a2bb5}Width = [info['width']] | Height = [info['height']]" text_size 16 at center

                            label "{color=0a2bb5}Bytes per pixel = [info['bpp']]" text_size 16 at center

                        hbox:
                            xsize 402 yalign 1.0
                            textbutton "{color=#4f7649}Apply current parameters for\nthe storage calculation." action [
                              SetVariable("image_width", info['width']),
                              SetVariable("image_height", info['height']),
                              SetVariable("image_bytes_pixel", info['bpp']),
                              Function(update_layers_max)
                            ] xalign 0.0 text_size 16

                        textbutton "{color=#4f7649}Return" action [
                          SetVariable("show_current_image_parameters", False)
                        ] xalign 1.0 yalign 1.0 text_size 16

                null height 2


label image_loop:
    if rotate_range < 0:
        $ rotate_range = 0
    if zoom_range < 0:
        $ zoom_range = 0.00
    if xalign_range < 0:
        $ xalign_range = 0.00
    if yalign_range < 0:
        $ yalign_range = 0.00
    #hide screen image_move
    #show screen image_move
    $ renpy.pause(hard=True)


label anim_progress_bar:
    while progress_bar < 100:
        $ progress_bar += 1
        $ renpy.pause(0.001, hard = True)
    $ progress_bar = 0
    if show_saving:
        jump save_layer_data
    if show_deleting:
        jump delete_layer_data


label list_image_files:
    python:
        image_dir = "images/"
        for image_list in renpy.list_files():
            if image_list.startswith(image_dir):
                if ((file_location == image_list)
                    and ((".png" in image_list)
                    or (".jpg" in image_list)
                    or (".jpeg" in image_list)
                    or (".webp" in image_list)
                    or (".avif" in image_list)
                    or (".svg" in image_list))):
                    renpy.jump("load_image")
        else:
            image_loading_error = True
            renpy.pause(hard = True)


label input_image:
    if stop_loading_layers:
        $ show_stop_message = True
        jump image_loop

    $ show_input_frame = True
    $ show_file_input = True
    $ location_input = "images/"

    call screen wait_enter_only

    if location_input == "images/":
        jump input_image

    $ file_location = (location_input)
    $ h_flip = False
    $ v_flip = False
    $ show_input_frame = False
    $ show_file_input = False

    jump list_image_files


label input_rotate:
    $ show_input_frame = True
    $ show_rotate_input = True
    $ number_input = ""

    call screen wait_enter_only

    $ show_input_frame = False
    $ show_rotate_input = False

    if number_input == "":
        $ number_input = "1"

    $ rotate_range = int(number_input)
    jump image_loop


label input_zoom:
    $ show_input_frame = True
    $ show_zoom_input = True
    $ float_input = ""
    $ float_value = 0.01

    call screen wait_enter_only

    $ show_input_frame = False
    $ show_zoom_input = False

    if (float_input == ""
        or float_input == "."
        or float_input == ".."
        or float_input == "..."
        or float_input == "...."):
        $ float_value = 0.01
    else:
        $ float_value = float(float_input)

    if (float_value < 0.01
        or float_value > 1.00):
        $ float_value = 0.01
        $ show_zoom_input = False
        $ show_invalid_float_message = True

    $ zoom_range = float_value
    jump image_loop


label input_xalign:
    $ show_input_frame = True
    $ show_xalign_input = True
    $ float_input = ""
    $ float_value = 0.01

    call screen wait_enter_only

    $ show_input_frame = False
    $ show_xalign_input = False

    if (float_input == ""
        or float_input == "."
        or float_input == ".."
        or float_input == "..."
        or float_input == "...."):
        $ float_value = 0.01
    else:
        $ float_value = float(float_input)

    if (float_value < 0.01
        or float_value > 1.00):
        $ float_value = 0.01
        $ show_xalign_input = False
        $ show_invalid_float_message = True

    $ xalign_range = float_value
    jump image_loop


label input_yalign:
    $ show_input_frame = True
    $ show_yalign_input = True
    $ float_input = ""
    $ float_value = 0.01

    call screen wait_enter_only

    $ show_input_frame = False
    $ show_yalign_input = False

    if (float_input == ""
        or float_input == "."
        or float_input == ".."
        or float_input == "..."
        or float_input == "...."):
        $ float_value = 0.01
    else:
        $ float_value = float(float_input)

    if (float_value < 0.01
        or float_value > 1.00):
        $ float_value = 0.01
        $ show_yalign_input = False
        $ show_invalid_float_message = True

    $ yalign_range = float_value
    jump image_loop


label input_image_size:
    $ number_input = ""

    if not image_width_entered:
        $ image_width_entered = True
        $ show_input_frame = True

        call screen wait_enter_only

        if number_input == "":
            $ number_input = "1920"
        $ image_width = int(number_input)
        $ image_width_entered = False

        $ number_input = ""
        $ image_height_entered = True
        $ show_input_frame = True
        call screen wait_enter_only
        if number_input == "":
            $ number_input = "1080"
        $ image_height = int(number_input)
        $ image_height_entered = False

        $ number_input = ""
        $ image_by_pi_entered = True
        $ show_input_frame = True
        call screen wait_enter_only
        if number_input == "":
            $ number_input = "4"
        $ image_bytes_pixel = int(number_input)
        $ image_by_pi_entered = False
        $ show_input_frame = False

        $ update_layers_max()

        jump image_loop


label get_image_info:
    python:
        start_path = subprocess.check_output(
            ["findmnt", "-rn", "-o", "TARGET"],
            text=True
        ).splitlines()

        current_directory = os.path.abspath(config.gamedir)

    $ info = get_image_info(current_directory + "/" + location_input)

    $ show_current_image_parameters = True

    jump image_loop

label load_dev_menu_save:
    $ slide_image_move_menu_right = False
    $ image_move_menu_startet = False
    $ move_into_screen = False
    $ reload_image_move = False
    $ keep_image_move = False
    $ renpy.pause(0.7, hard = True)
    $ renpy.load("main_game_save_dev")


label delete_image_move:
    python:
        reset_all_layers()
        selected_layer = -1
        layer = -1
        zoom_var = 1.0
        xzoom_var = 1.0
        yzoom_var = 1.0
        xalign_var = 0.5
        yalign_var = 0.5
        rotate_var = 0
        h_flip = False
        v_flip = False
        image_move_active = False
        layers_simultan = False
        show_deleting = False
        update_layers_max()
    $ delete_query = False
    $ move_into_screen = False
    $ renpy.pause(0.7, hard = True)
    $ renpy.load("main_game_save_dev")


label delete_layers_only:
    python:
        reset_all_layers()
        selected_layer = -1
        layer = -1
        zoom_var = 1.0
        xzoom_var = 1.0
        yzoom_var = 1.0
        xalign_var = 0.5
        yalign_var = 0.5
        rotate_var = 0
        h_flip = False
        v_flip = False
        image_move_active = False
        layers_simultan = False
        show_deleting = False
        image_found = False
        delete_query = False
        stop_loading_layers = False
        update_layers_max()
    jump image_loop


init python:
    from datetime import datetime

    class Layer:
        def __init__(self):
            self.layer = -1
            self.active = False
            self.image = None

            self.zoom = 1.0
            self.xzoom = 1.0
            self.yzoom = 1.0

            self.xalign = 0.5
            self.yalign = 0.5

            self.rotate = 0

            self.diff_rotate = 0
            self.diff_zoom = 0
            self.diff_xalign = 0
            self.diff_yalign = 0

            self.h_flip = False
            self.v_flip = False

        def reset(self):
            self.layer = -1
            self.active = False
            self.image = None

            self.zoom = 1.0
            self.xzoom = 1.0
            self.yzoom = 1.0

            self.xalign = 0.5
            self.yalign = 0.5

            self.rotate = 0

            self.diff_rotate = 0
            self.diff_zoom = 0
            self.diff_xalign = 0
            self.diff_yalign = 0

            self.h_flip = False
            self.v_flip = False

        def show(self, layer):
            renpy.show(
                "layer_" + str(layer),
                what = renpy.display.im.image(self.image),
                at_list = [
                    Transform(
                        rotate = self.rotate,
                        zoom = self.zoom,
                        xzoom = self.xzoom,
                        yzoom = self.yzoom,
                        xalign = self.xalign,
                        yalign = self.yalign
                    )
                ]
            )

        def update_flip(self):
            zoom_x = abs(self.xzoom)
            zoom_y = abs(self.yzoom)
            self.xzoom = zoom_x * (-1 if self.h_flip else 1)
            self.yzoom = zoom_y * (-1 if self.v_flip else 1)


    # Variable Layer-Slots
    layer_slots = []

    # Auswahl des aktuell markierten Layers
    def get_selected_layer():
        if selected_layer > -1:
            return layer_slots[selected_layer]
        return None

    def toggle_flip_h():
        layer = get_selected_layer()

        if layer:
            layer.h_flip = not layer.h_flip
            layer.update_flip()
            layer.show(selected_layer)

    def toggle_flip_v():
        layer = get_selected_layer()

        if layer:
            layer.v_flip = not layer.v_flip
            layer.update_flip()
            layer.show(selected_layer)

    def reset_all_layers():
        for layer, current_layer in enumerate(layer_slots):
            if current_layer.active:
                renpy.hide("layer_" + str(layer))
                current_layer.reset()

    def save_dev_menu():
        renpy.save("main_game_save_dev")

    def show_date_time():
        now = datetime.now()
        return now.strftime("%B %d, %Y, %H:%M:%S")


label load_image:
    if (not move_layers_simultan
        and not stop_loading_layers):
        $ layer += 1
        $ selected_layer = layer
        $ zoom_var = 1.0
        $ xzoom_var = 1.0
        $ yzoom_var = 1.0
        $ xalign_var = 0.50
        $ yalign_var = 0.50
        $ rotate_var = 0

        while len(layer_slots) <= layer:
            $ layer_slots.append(Layer())

        $ current_layer = layer_slots[layer]

        $ current_layer.active = True
        $ current_layer.image = file_location

        if h_flip:
            $ current_layer.xzoom = -1
        else:
            $ current_layer.xzoom = 1

        if v_flip:
            $ current_layer.yzoom = -1
        else:
            $ current_layer.yzoom = 1

        $ current_layer.rotate = rotate_var
        $ current_layer.xalign = xalign_var
        $ current_layer.zoom = zoom_var
        $ current_layer.yalign = yalign_var

        $ image_found = False

        $ current_layer.show(layer)

        $ update_layers_max()

        if (layers_max < 10
            and not stop_loading_layers):
            $ stop_loading_layers = True
            $ show_stop_message = True
            show screen image_move

    jump image_loop


label restart_image:
    python:
        if move_layers_simultan:

            # Aktuell ausgewählten Layer holen.
            selected = layer_slots[selected_layer]

            # Änderungen des aktuell ausgewählten Layers ermitteln
            diff_rotate = round(
                rotate_var - selected.rotate, 2
            )

            diff_zoom = round(
                zoom_var - selected.zoom, 2
            )

            diff_xalign = round(
                xalign_var - selected.xalign, 2
            )

            diff_yalign = round(
                yalign_var - selected.yalign, 2
            )

            # Ermitteln, ob sich der Flip-Zustand geändert hat.
            flip_h_changed = h_flip != selected.h_flip
            flip_v_changed = v_flip != selected.v_flip

            # Alle aktiven Layer bearbeiten
            for layer, current_layer in enumerate(layer_slots):

                if current_layer.active:

                    # Position relativ zur bisherigen Position verändern.
                    current_layer.rotate = round(
                        current_layer.rotate + diff_rotate, 2
                    )

                    current_layer.zoom = round(
                        current_layer.zoom + diff_zoom, 2
                    )

                    current_layer.xalign = round(
                        current_layer.xalign + diff_xalign, 2
                    )

                    current_layer.yalign = round(
                        current_layer.yalign + diff_yalign, 2
                    )

                    # ----------------------------------------
                    # HORIZONTAL FLIP
                    # ----------------------------------------
                    #
                    # Nur wenn sich der Flip beim ausgewählten
                    # Layer tatsächlich geändert hat, wird bei
                    # allen Layern ebenfalls umgeschaltet.
                    #
                    if flip_h_changed:
                        current_layer.h_flip = not current_layer.h_flip

                    # ----------------------------------------
                    # VERTIKAL FLIP
                    # ----------------------------------------
                    #
                    if flip_v_changed:
                        current_layer.v_flip = not current_layer.v_flip

                    # Zoom-Vorzeichen entsprechend dem
                    # individuellen Flip-Zustand aktualisieren.
                    current_layer.update_flip()

                    # Layer neu anzeigen
                    current_layer.show(layer)


        if not move_layers_simultan:

            if selected_layer >= 0 and selected_layer < len(layer_slots):

                current_layer = layer_slots[selected_layer]

                if current_layer.active:

                    # Individuellen Flip-Zustand speichern.
                    current_layer.h_flip = h_flip
                    current_layer.v_flip = v_flip
                    current_layer.update_flip()

                    # Position, Zoom und Rotation.
                    current_layer.xalign = round(xalign_var, 2)
                    current_layer.yalign = round(yalign_var, 2)
                    current_layer.zoom = round(zoom_var, 2)
                    current_layer.rotate = rotate_var

                    # Bild aktualisieren.
                    current_layer.show(selected_layer)

    jump image_loop


label restart_layer_counter:
    python:
        selected_layer += 1

        if selected_layer > layer:
            selected_layer = 0

        if selected_layer == -1:
            zoom_var = 1.0
            xzoom_var = 0.00
            yzoom_var = 0.00
            xalign_var = 0.00
            yalign_var = 0.00
            rotate_var = 0
            h_flip = False
            v_flip = False

        else:
            current_layer = layer_slots[selected_layer]

            # Falls der Layer nicht existiert
            if not current_layer.active:
                selected_layer = -1

            else:
                xzoom_var = abs(current_layer.xzoom)
                yzoom_var = abs(current_layer.yzoom)

                xalign_var = current_layer.xalign
                yalign_var = current_layer.yalign
                zoom_var = current_layer.zoom
                rotate_var = current_layer.rotate

                h_flip = current_layer.h_flip
                v_flip = current_layer.v_flip

    jump image_loop


label save_layer_data:
    $ persistent.data_position_file = True
    $ show_saving = False

    python:
        current_directory = os.getcwd()
        file_path = os.path.join(
            current_directory,
            "image_positioning_tool",
            "game",
            "scripts",
            "layer_positions.txt"
        )

        get_date_time = show_date_time()

        with open(file_path, "a") as file:
            file.write("\n\n{b}________________________________________________{/b}")
            file.write("\n\n{b}Layer data on: {/b}" + "{b}" + get_date_time + "{/b}")

            for layer, current_layer in enumerate(layer_slots):
                if current_layer.active:
                    file.write("\n\n{b}Layer " + str(layer) + "{/b}")
                    file.write("\nPath and filename: " + str(current_layer.image))
                    file.write("\nXZoom: " + str(current_layer.xzoom))
                    file.write("\nYZoom: " + str(current_layer.yzoom))
                    file.write("\nRotate: " + str(current_layer.rotate))
                    file.write("\nXalign: " + str(current_layer.xalign))
                    file.write("\nYalign: " + str(current_layer.yalign))
                    file.write("\nHorizontal Flip: " + str(current_layer.h_flip))
                    file.write("\nVertical Flip: " + str(current_layer.v_flip) + "\n")

    jump image_loop


label show_layer_pos_txt:
    $ text = renpy.file("scripts/layer_positions.txt").read().decode("utf-8")
    show screen show_data_pos_file(text) with Dissolve(0.2)
    $ renpy.pause(hard=True)


label delete_layer_data:
    $ persistent.data_position_file = False
    $ show_deleting = False
    python:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, "image_positioning_tool", "game", "scripts", 'layer_positions.txt')
        file = open(file_path, "w")
        file.write("")
        file.close()
    jump image_loop


#######################
# Projektinstallation #
#######################


transform search_projects_menu_hide:
    yalign 0.12

transform search_projects_menu_show:
    yalign 0.12
    ease 0.3 yalign 0


screen search_projects_menu():
    frame:
        background Solid("#2e4a2a")
        padding(4, 2)
        xalign 0.5

        if search_projects_menu_opened:
            at search_projects_menu_show

        else:
            at search_projects_menu_hide

        vbox:
            xalign 0.5
            null height 2

            if not store.search_running:
                textbutton "{color=#4f7649}Search for RenPy projects" action [
                    Hide("found_projects_screen", transition = Dissolve(0.2)),
                    Jump("search_projects"),
                ] style "ipt_button" text_style "ipt_center_button_text" xsize 300

                null height 2

            if store.search_running:
                textbutton "Cancel search" action [
                    Function(cancel_search)
                ] style "ipt_button" text_style "ipt_center_button_text" xsize 300

                null height 2

            if not store.search_running:
                textbutton "{color=#4f7649}Return" action [
                    Hide("found_projects_screen", transition = Dissolve(0.2)),
                    SetVariable("start_search_menu", False),
                    SetVariable("data_project_file", False),
                    MainMenu(confirm = False)
                ] style "ipt_button" text_style "ipt_center_button_text" xsize 300

                null height 2

            if store.search_running:
                textbutton "Return" style "ipt_button" text_style "ipt_center_button_text" xsize 300

                null height 2

    # Nach Animation laden
    if load_projects_after_slide:
        timer 0.3 action [
            SetVariable("load_projects_after_slide", False),
            Function(load_found_projects),
            Show("found_projects_screen", transition=Dissolve(0.2))
        ]


screen found_projects_screen():
    frame:
        background Solid("#2e4a2a")
        ypos 48 xsize 800 ysize 552
        padding(4, 4, 4, 4)

        fixed:
            xsize 996 ysize 545

            viewport:
                id "found_projects_viewport"
                mousewheel True
                draggable True

                vbox:
                    spacing 5
                    for project in found_project_buttons:
                        textbutton project["display"]:
                            xsize 780
                            style "ipt_button"
                            text_style "ipt_button_text"

                            sensitive not message_window_open
                            action Function(project_clicked, project["path"])

            vbar:
                value YScrollValue("found_projects_viewport")
                xpos 785
                xsize 8
                ysize 545

                thumb "#4f7649"
                base_bar "#7ede69"


screen message_window(message):
    fixed:
        xsize 600
        ysize 250
        xalign 0.5
        yalign 0.5
        frame:
            background "#96d089"
            xsize 600
            ysize 250

            if not error_found:
                viewport:
                    id "message_viewport"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 5
                        text "[message]" style "ipt_text" xmaximum 520

                vbar:
                    value YScrollValue("message_viewport")
                    xpos 580
                    xsize 8
                    thumb "#4f7649"
                    base_bar "#7ede69"

            if error_found:

                viewport:
                    id "error_viewport"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 5
                        text "{color=#cd1e1e}{b}Could not load file:{/b}{/color}" size 18 font ipt_font
                        text "{color=#cd1e1e}[message]" size 18 xmaximum 520 font ipt_font

                vbar:
                    value YScrollValue("error_viewport")
                    xpos 580
                    xsize 8
                    thumb "#4f7649"
                    base_bar "#7ede69"

        textbutton "Close window" action [
            SetVariable("message_window_open", False),
            Hide("message_window", transition=Dissolve(0.2))
        ] xpos 437 ypos 249 text_size 18 text_font ipt_font


default search_progress = 0
default search_display_progress = 0
default search_status = ""
default search_running = False
default search_finished = False
default search_matches = []
default collecting_dots = ""
default search_current_file = ""
default search_current_path = ""
default found_project_buttons = []
default search_projects_menu_opened = False
default load_projects_after_slide = False
default message_window_open = False
default search_cancel_requested = False


screen search_progress():
    timer 0.05 repeat True action [
        Function(update_fake_progress)
    ]

    timer 0.4 repeat True action [
        Function(update_collecting_animation)
    ]

    frame:
        background Solid("#2e4a2a")
        xalign 0.5 yalign 0.5 xsize 700 ysize 300
        padding(4, 4, 4, 4)
        vbox:
            xalign 0.5
            frame:
                background Solid("84ec6e")
                padding(4, 4, 4, 4)
                hbox:
                    text "[search_status] [collecting_dots]" style "ipt_text"
                    if not store.search_status == "\"label start:\" searching [collecting_dots]":
                        pass

                text "\n\n\nSearch path: [store.search_current_path]":
                    xmaximum 680
                    style "ipt_text"

                text "\n\n\n\n\n\nSearch files: [search_current_file]":
                    xmaximum 680
                    style "ipt_text"

                frame:
                    background Solid("#2e4a2a")
                    padding(4, 4)
                    xalign 0.99 yalign 0.75
                    vbox:
                        if data_project_file:
                            textbutton "Show RenPy projects" action [
                                    SetVariable("search_projects_menu_opened", True),
                                    SetVariable("load_projects_after_slide", True),
                                    SetVariable("search_finished", True)
                                ] style "ipt_button" text_style "ipt_center_button_text" xsize 260

                            textbutton "Delete RenPy projects data" action [
                                    SetVariable("data_project_file", False)
                                ] style "ipt_button" text_style "ipt_center_button_text" xsize 260

                        if not data_project_file:
                            textbutton "Show RenPy projects" style "ipt_button" text_style "ipt_center_button_text" xsize 260

                            textbutton "Delete RenPy projects data" style "ipt_button" text_style "ipt_center_button_text" xsize 260

                frame:
                    xalign 0.5 yalign 1.0 xsize 680 ysize 45
                    vbox:
                        xalign 0.5
                        spacing 8

                        bar:
                            value search_display_progress
                            range 100

                            # Farben definieren
                            left_bar Solid("#2e4a2a")    # Gefüllter Fortschritt
                            right_bar Solid("#4f7649")   # Ungefüllter Hintergrund

                            # Dimensionen festlegen (wichtig, damit die Bar sichtbar wird)
                            xsize 680
                            ysize 20

                            # Verhindert, dass der "Thumb" (Schieberegler) angezeigt wird
                            thumb None

                        text "[int(search_display_progress)] %":
                            xalign 0.5 style "ipt_text"

                    if search_finished:
                        timer 0.1 action [
                            Return()
                        ]


init python:
    import time
    import shutil

    EXCLUDED_DIRS = ["launcher", "gui", "assets"]

    SEARCH_TEXT = "label start:"

    def get_allowed_mountpoints():

        # Hier werden die Mountpoints gespeichert,
        # die durchsucht werden dürfen.
        allowed_mountpoints = []

        try:

            # Informationen über die Laufwerke abfragen.
            result = subprocess.run(
                [
                    "lsblk",
                    "-r",
                    "-n",
                    "-o",
                    "TYPE,MOUNTPOINT"
                ],
                capture_output=True,
                text=True,
                check=True
            )


        except (
            subprocess.CalledProcessError,
            FileNotFoundError,
            OSError
        ):

            # Falls lsblk nicht ausgeführt werden kann,
            # keine Mountpoints zurückgeben.
            return []


        # Jede Zeile der lsblk-Ausgabe bearbeiten.
        for line in result.stdout.splitlines():
            parts = line.split(maxsplit=1)

            # Ungültige oder unvollständige Zeilen überspringen.
            if len(parts) < 2:
                continue

            device_type = parts[0]
            mountpoint = parts[1]

            # Kein Mountpoint vorhanden.
            if not mountpoint:
                continue

            # Optische Laufwerke ausschließen.
            if device_type == "rom":
                continue

            allowed_mountpoints.append(mountpoint)

        return allowed_mountpoints

    def update_collecting_animation():
        if not store.search_running:
            store.collecting_dots = ""
            return

        if (store.search_status.startswith("Collecting")
            or store.search_status.startswith("\"label start:\" searching")):
            if store.collecting_dots == "":
                store.collecting_dots = "."
            elif store.collecting_dots == ".":
                store.collecting_dots = ". ."
            elif store.collecting_dots == ". .":
                store.collecting_dots = ". . ."
            else:
                store.collecting_dots = ""

    def update_fake_progress():

        if not store.search_running:
            return

        real = store.search_progress
        fake = store.search_display_progress

        diff = real - fake


        # Weiche Bewegung

        if diff > 15:
            speed = 0.45

        elif diff > 5:
            speed = 0.25

        elif diff > 0:
            speed = 0.12

        else:
            speed = 0.03

        fake += diff * speed


        # kleine Bewegung gegen Stillstand

        if real < 99 and fake < real:
            fake += 0.05


        # niemals vorauslaufen

        if fake > real + 1:
            fake = real + 1


        # während Suche begrenzen

        if store.search_running:
            fake = min(fake, 99.2)

        store.search_display_progress = fake


    def shorten_path(path, max_length=100):
        if len(path) <= max_length:
            return path

        part_length = (max_length - 5) // 2

        return (
            path[:part_length]
            + " ... "
            + path[-part_length:]
        )


    def search_thread(start_dir = None):
        output_file = os.path.join(
            store.OUTPUT_DIR,
            "scripts/renpy_label_start_found.txt"
        )

        store.search_running = True
        store.search_cancel_requested = False
        store.search_finished = False
        store.search_progress = 0
        store.search_display_progress = 0
        store.search_matches = []
        store.search_current_file = ""
        store.search_current_path = ""
        start_time = time.time()


        # --------------------------------
        # Phase 1:
        # Alle rpy Dateien sammeln
        # --------------------------------

        store.search_status = (
            "Collecting rpy files"
        )

        all_files = []

        global search_current_path

        for root, dirs, files in os.walk(start_dir):
            parts = os.path.normpath(root).split(os.sep)

            # Aktuell durchsuchten Ordner anzeigen
            search_current_path = shorten_path(root)

            if store.search_cancel_requested:
                store.search_running = False
                store.search_status = "Search cancelled."
                return

            # Ausgeschlossene Ordner nicht durchsuchen
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            parts = os.path.normpath(root).split(os.sep)

            if "game" not in parts:
                continue

            for file in files:
                if file.lower().endswith(".rpy"):
                    all_files.append(
                        os.path.join(root, file)
                    )

        total_files = len(all_files)



        # --------------------------------
        # Phase 2:
        # Dateien durchsuchen
        # --------------------------------

        checked = 0

        for path in all_files:
            if store.search_cancel_requested:
                store.search_running = False
                store.search_status = "Search cancelled."
                return

            checked += 1


            # echter Fortschritt

            if total_files:

                store.search_progress = (
                    checked / total_files * 100
                )

            else:

                store.search_progress = 100

            store.search_status = (
                "\"label start:\" searching"
            )
            store.search_current_file = path

            try:
                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"

                ) as f:
                    for lineno, line in enumerate(f, 1):
                        if SEARCH_TEXT in line:
                            store.search_matches.append(
                                "{} (Line {})".format(
                                    path,
                                    lineno
                                )
                            )
                            break

            except Exception:
                pass

        elapsed = time.time() - start_time


        # Ergebnisdatei schreiben

        try:
            with open(output_file, "w", encoding="utf-8") as out:
                for line in store.search_matches:
                    path = line.split(" (Line")[0]
                    game_marker = os.sep + "game" + os.sep

                    if game_marker in path:
                        # kompletten Trefferpfad speichern
                        formatted = path
                        out.write(formatted + "\n")
                        store.data_project_file = True
                    else:
                        out.write(path + "\n")

        except Exception as e:
            store.error_found = True
            store.message_window_open = True
            renpy.show_screen("message_window", message = "\n{}".format(e))
            renpy.transition(Dissolve(0.2))
            renpy.pause(hard = True)

        store.search_status = (
            f"Search complete.  |  Search time: {elapsed:.2f} seconds.  |  {len(store.search_matches)} files found."
        )


        # Abschluss

        store.search_progress = 100
        store.search_display_progress = 100
        store.search_running = False

    def load_found_projects():
        store.found_project_buttons = []

        filename = os.path.join(
            store.OUTPUT_DIR,
            "scripts/renpy_label_start_found.txt"
        )

        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()

                    if line:
                        game_marker = os.sep + "game" + os.sep
                        display = line
                        if game_marker in line:
                            before_game = line.split(game_marker)[0]
                            folder_name = os.path.basename(before_game)
                            display = (
                                line.replace(
                                    folder_name,
                                    "{b}" + folder_name + "{/b}",
                                    1
                                )
                            )

                        store.found_project_buttons.append(
                            {
                                "path": line,
                                "display": display
                            }
                        )

        except Exception as e:
            store.error_found = True
            store.message_window_open = True
            renpy.show_screen("message_window", message = "\n{}".format(e))
            renpy.transition(Dissolve(0.2))
            renpy.pause(hard = True)

    # def project_clicked(project):
    #     message = ""
    #
    #     try:
    #         project_path = os.path.normpath(project)
    #
    #         if os.path.isfile(project_path):
    #             # project ist bereits die Datei
    #             script_file = project_path
    #
    #             # Normalerweise: .../game/script.rpy -> .../game
    #             game_path = os.path.dirname(script_file)
    #
    #             # Falls die Datei in .../game/scripts liegt
    #             if os.path.basename(game_path).casefold() == "scripts":
    #                 game_path = os.path.dirname(game_path)
    #
    #         else:
    #             # project ist ein Ordner
    #             if os.path.basename(project_path).casefold() == "scripts":
    #                 game_path = os.path.dirname(project_path)
    #             else:
    #                 game_path = project_path
    #
    #             script_file = os.path.join(
    #                 game_path,
    #                 "script.rpy"
    #             )


    def project_clicked(project):
        message = ""

        try:
            project_path = os.path.normpath(project)

            # 1. Startpunkt festlegen & Basispfad bestimmen
            if os.path.isfile(project_path):
                current_dir = os.path.dirname(project_path)
            else:
                current_dir = project_path

            # Falls wir uns bereits in 'game' oder einem Unterordner davon befinden,
            # navigieren wir hoch bis zum eigentlichen 'game'-Ordner.
            game_path = None
            parts = current_dir.split(os.sep)

            # Suchen nach dem Ordner 'game' in der Pfadstruktur
            for i in range(len(parts) - 1, -1, -1):
                if parts[i].casefold() == "game":
                    game_path = os.sep.join(parts[: i + 1])
                    break

            # Falls 'game' nicht im Pfad enthalten ist, nehmen wir das übergebene Verzeichnis als Basis
            if not game_path:
                game_path = current_dir

            # 2. Rekursiv nach der ersten .rpy-Datei innerhalb von game_path suchen
            found_script = None
            for root, dirs, files in os.walk(game_path):
                for file in files:
                    if file.casefold() == "script.rpy":
                        found_script = os.path.join(root, file)
                        break
                if found_script:
                    break

            # 3. Überprüfung und Auswertung
            if not found_script:
                message = f"Keine .rpy-Datei in '{game_path}' oder deren Unterordnern gefunden."
            else:
                script_file = found_script
                # game_path ist hier garantiert auf das Hauptverzeichnis /game festgelegt
                print(f"Game-Pfad: {game_path}")
                print(f"Gefundene Skript-Datei: {script_file}")

            if not os.path.isfile(script_file):
                message = (
                    "Datei nicht gefunden:\n{}"
                    .format(script_file)
                )

            else:
                with open(
                    script_file,
                    "r",
                    encoding="utf-8-sig"
                ) as f:
                    original_lines = f.readlines()

                overlay_line = (
                    '    config.overlay_screens.append("image_move_hidden")\n\n'
                    'python:\n'
                    '    update_layers_max()\n'
                )


                if overlay_line not in original_lines:

                    # Entfernt alle leeren Zeilen am Anfang
                    while (
                        original_lines
                        and original_lines[0].strip() == ""
                    ):
                        original_lines.pop(0)


                    # Entfernt unsichtbare Zeichen vor der ersten echten Zeile
                    if original_lines:

                        original_lines[0] = (
                            original_lines[0].lstrip(
                                " \t\r\n\uFEFF"
                            )
                        )

                    new_lines = []

                    new_lines.append(
                        "init python:\n"
                    )

                    new_lines.append(
                        overlay_line
                    )

                    new_lines.append(
                        "\n"
                    )

                    new_lines.extend(
                        original_lines
                    )

                    with open(
                        script_file,
                        "w",
                        encoding="utf-8",
                        newline=""
                    ) as f:
                        f.writelines(
                            new_lines
                        )

                    message = (
                        "{{color=#238626}}Added:{{/color}}\n"
                        "config.overlay_screens.append(\"image_move_hidden\")\n\n"
                        "File:\n{}".format(
                            script_file
                        )
                    )

                else:

                    message = (
                        "{{color=#238626}}Line already exists:{{/color}}\n{}".format(
                            script_file
                        )
                    )

                source_files = [
                    "developer_menu.rpy",
                    "version_ipt.rpy",
                    "layer_positions.txt",
                    "00_ipt_system.rpy"
                ]

                target_scripts_folder = game_path

                search_folders = [
                    os.path.join(store.OUTPUT_DIR, ""),
                    os.path.join(store.OUTPUT_DIR, "scripts")
                ]

                for filename in source_files:
                    source_file = None


                    # Erst scripts suchen
                    # danach game

                    for folder in search_folders:
                        possible_file = os.path.join(
                            folder,
                            filename
                        )

                        if os.path.isfile(possible_file):
                            source_file = possible_file
                            break

                    target_file = os.path.join(
                        target_scripts_folder,
                        filename
                    )

                    if source_file:
                        shutil.copyfile(
                            source_file,
                            target_file
                        )

                        message += (
                            "\n\n{{color=#238626}}Copied: {{b}}{}{{/b}}:{{/color}}\n{}"
                            .format(
                                filename,
                                target_file
                            )
                        )

                    else:

                        message += (
                            "\n\nWarning:\n"
                            "{} not found:\n{}"
                            .format(
                                filename,
                                source_file
                            )
                        )

                # Quellprojekt:
                # store.OUTPUT_DIR/game/psutil
                source_psutil = os.path.join(
                    store.OUTPUT_DIR,
                    "psutil"
                    )

                # Zielprojekt:
                # .../game/psutil
                target_psutil_folder = game_path

                target_psutil = os.path.join(
                    target_psutil_folder,
                    "psutil"
                )

                if os.path.isdir(source_psutil):
                    shutil.copytree(
                        source_psutil,
                        target_psutil,
                        dirs_exist_ok=True
                        )

                    message += (
                        "\n\n{{color=#238626}}Copied {{b}}psutil{{/b}} folder:{{/color}}\n{}"
                        .format(
                            target_psutil
                        )
                    )

                else:

                    message += (
                        "\n\nWarning:\n"
                        "psutil folder not found:\n{}"
                        .format(
                            source_psutil
                        )
                    )


                ##################
                # Fonts kopieren #
                ##################

                fonts_source_files = [
                    "DejaVuSansMono.ttf"
                ]

                # Ziel: .../game/Fonts
                target_fonts_folder = os.path.join(
                    game_path,
                    "Fonts"
                )

                # Fonts-Ordner im Zielprojekt erzeugen
                os.makedirs(
                    target_fonts_folder,
                    exist_ok=True
                )

                # Quelle: OUTPUT_DIR/Fonts
                search_fonts_folder = [
                    os.path.join(
                        store.OUTPUT_DIR,
                        "Fonts"
                    )
                ]

                for font_filename in fonts_source_files:
                    font_source_file = None

                    # Quelldatei suchen
                    for fonts_folder in search_fonts_folder:
                        possible_font_file = os.path.join(
                            fonts_folder,
                            font_filename
                        )

                        if os.path.isfile(possible_font_file):
                            font_source_file = possible_font_file
                            break

                    # Wenn keine Quelle gefunden wurde
                    if font_source_file is None:
                        message += (
                            "\n\nWarning:\n"
                            "{} not found in:\n{}"
                            .format(
                                font_filename,
                                search_fonts_folder
                            )
                        )
                        continue

                    # Zielpfad bilden
                    target_font_file = os.path.join(
                        target_fonts_folder,
                        font_filename
                    )

                    # Datei kopieren
                    shutil.copyfile(
                        font_source_file,
                        target_font_file
                    )

                    message += (
                        "\n\n{{color=#238626}}Copied: "
                        "{{b}}{}{{/b}}:{{/color}}\n{}"
                        .format(
                            font_filename,
                            target_font_file
                        )
                    )


            store.message_window_open = True

            renpy.show_screen(
                "message_window",
                message=message
            )

            renpy.transition(
                Dissolve(0.2)
            )

        except Exception as e:

            store.error_found = True
            store.message_window_open = True

            renpy.show_screen(
                "message_window",
                message="\n{}".format(e)
            )

            renpy.transition(
                Dissolve(0.2)
            )

    def cancel_search():
        store.search_cancel_requested = True

        if store.search_cancel_requested:
            store.search_running = False
            store.search_progress = 0
            store.search_display_progress = 0
            store.search_current_file = ""
            store.search_status = "Search cancelled."
            return


label search_projects:
    $ search_projects_menu_opened = False
    show screen search_projects_menu

    $ START_DIR = "/home/daniel/Daten/"

    python:
        current_directory = os.path.abspath(config.gamedir)

    $ OUTPUT_DIR = current_directory

    show screen search_progress with Dissolve(0.2)
    $ renpy.invoke_in_thread(search_thread, START_DIR)
    call screen search_progress
    show screen found_projects_screen with Dissolve(0.2)
    $ renpy.restart_interaction()
    $ renpy.pause(hard = True)



