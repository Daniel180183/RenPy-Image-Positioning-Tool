

init -1 python hide:
    config.screen_width = 1000
    config.screen_height = 720

    style.say_who_window.background = Frame("images/mp.png", 40, 40)
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0

    # Position small dialogue Box
    style.say_who_window.xpos = -4
    style.say_who_window.ypos = 46

    style.say_who_window.left_padding = 15
    style.say_who_window.top_padding = 15
    style.say_who_window.right_padding = 15
    style.say_who_window.bottom_padding = 15
    style.say_who_window.xminimum = 300
    style.say_who_window.yminimum = 50

    config.window_title = project_name

    config.name = project_name
    config.version = project_version

    theme.threeD(
        # Button and slider background colour unhovered
        widget = "#84ec6e",

        # Button and slider background colour hovered
        widget_hover = "#b8f4b8",

        # Button text and unselected widget colour
        widget_text = "#4f7649",

        # Selected widget text colour
        widget_selected = "#65b058",

        # Disabled widget background colour
        disabled = "#79b971",

        # Disabled widget text colour
        disabled_text = "#5b864a",

        # Label over button
        label = "#d6e9d0",

        # Menu frames
        frame = "#77c966",

        mm_root = "background",

        gm_root = "background",

        rounded_window = False,

        )


    style.window.background = Frame("images/mp.png", 12, 12)

    style.window.left_margin = 1
    style.window.right_margin = 1
    style.window.top_margin = 1
    style.window.bottom_margin = 1

    style.window.left_padding = 60
    style.window.right_padding = 260
    style.window.top_padding = 35
    style.window.bottom_padding = 35

    # Y-text position in main frame
    style.window.yminimum = 175

    style.default.font = "Fonts/Bubble Sans 1.01.otf"

    style.default.size = 22

    style.default.color = "#000000" 

    config.has_sound = True


    config.has_music = True


    config.has_voice = False


    #style.button.activate_sound = "audio/click3.mp3"
    #style.imagemap.activate_sound = "audio/click3.mp3"

    #config.enter_sound = "audio/click3.mp3"
    #config.exit_sound = "audio/click3.mp3"

    #config.sample_sound = "audio/click3.mp3"

    #config.main_menu_music = "audio/Dreamer.mp3"


    #config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None

python early:
    config.save_directory = "Avatar Harem-1467471742"

init -1 python hide:
    config.default_fullscreen = False
    config.default_text_cps = 42
    config.default_afm_time = 10
    config.window_icon = "icon.png"


init python:
    build.directory_name = "Image_Positioning_Tool"

    build.executable_name = "Image_Positioning_Tool"

    build.include_update = False

    #build.classify('**~', None)
    #build.classify('**.bak', None)
    #build.classify('**/.**', None)
    #build.classify('**/#**', None)
    #build.classify('**.rpy', None)
    #build.classify('**.txt', None)
    #build.classify('**/thumbs.db', None)

    build.archive("scripts", "all")
    build.archive("images", "all")


    #build.classify("game/**.rpy", "scripts")
    #build.classify("game/**.rpyc", "scripts")

    #build.classify("game/**.jpeg", "images")
    #build.classify("game/**.jpg", "images")
    #build.classify("game/**.png", "images")
    #build.classify("game/**.ogg", "images")
    #build.classify("game/**.mp3", "images")
    #build.classify("game/**.wav", "images")

    build.documentation('*.html')
    build.documentation('*.txt')
