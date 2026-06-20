
init:
    $ slot = 0

default persistent.dialogueBoxOpacity = 0.9


screen choice(items):

    window:
        style "menu_window"
        if grab_menu_pos:
            xalign 0.907
            yalign 0.945
        else:
            xalign 0.5
            yalign 0.5

        has vbox
        style "menu"
        spacing 2

        for caption, action, chosen in items:

            if action:

                if "(locked)" in caption:
                    $ caption = caption.replace("(locked)", "")
                    button:
                        action None
                        if grab_menu_pos:
                            style "crab_menu_choice_button"
                            text caption style "menu_choice" size 17
                        else:
                            style "menu_choice_button"
                            text caption style "menu_choice"
                else:
                    button:
                        action action
                        if grab_menu_pos:
                            style "crab_menu_choice_button"
                            text caption style "menu_choice" size 17
                        else:
                            style "menu_choice_button"
                            text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.51)
        xmaximum int(config.screen_width * 0.51)
    style crab_menu_choice_button is button:
        xminimum int(config.screen_width * 0.48)
        xmaximum int(config.screen_width * 0.48)


screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text" color "#00008b"

    use quick_menu


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        style "nvl_vbox"

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox
                spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


screen main_menu():
    tag menu
    window:
        style "mm_root"

        text "{[project_name_color]}{size=17}{font=NotoSans-Bold.ttf}[project_name]{/font}{/size}{/color}" xpos 740 ypos 1
        text "{[project_name_color]}{size=17}{font=NotoSans-Bold.ttf}v[project_version]{/font}{/size}{/color}" xpos 950 ypos 1

    frame:
        style_group "mm"
        xalign .98
        yalign .97

        has vbox

        if renpy.android:
            spacing 15

            hbox:
                yalign .8
                textbutton _("New Game") action Start() text_size 18
                textbutton _("Load Game") action ShowMenu("load") text_size 18
                textbutton _("Preferences") action ShowMenu("preferences") text_size 18

        else:
            spacing 15
            vbox:
                textbutton _("New Game") action Start() text_size 16
                textbutton _("Load Game") action ShowMenu("load") text_size 16
                textbutton _("Preferences") action ShowMenu("preferences") text_size 16

            vbox:
                textbutton _("Quit") action Quit(confirm=False) text_size 16


init -2:
    style mm_button:
        size_group "mm"


screen navigation():
    window:
        style "gm_root"

    frame:
        style_group "gm_nav"
        xalign 0.99
        yalign 0.98
        padding(0,0)

        has hbox

        if renpy.android:
            vbox:
                textbutton _("Return") action Return() text_size 18
                textbutton _("Preferences") action ShowMenu("preferences") text_size 18
                textbutton _("Delete Game") action ShowMenu("delete") text_size 18
                textbutton _("Save Game") action ShowMenu("save") text_size 18
                textbutton _("Main Menu") action MainMenu() text_size 18
                textbutton _("Quit") action Quit() text_size 18
        else:
            vbox:
                textbutton _("Return") action Return() text_size 18
                textbutton _("Preferences") action ShowMenu("preferences") text_size 18
                textbutton _("Delete Game") action ShowMenu("delete") text_size 18
                textbutton _("Save Game") action ShowMenu("save") text_size 18
                textbutton _("Main Menu") action MainMenu("main_menu") text_size 18
                textbutton _("Quit") action Quit() text_size 18

    frame:
        style_group "gm_nav"
        xalign 0.008
        yalign 0.7
        padding(0,0)

        has hbox
        vbox:
            textbutton "Start" action Start() text_size 18


init -2:
    style gm_nav_button:
        size_group "gm_nav"


screen file_picker():
    frame:
        yminimum 430
        style "file_picker_frame"

        has vbox

        hbox:
            xcenter 500

            style_group "file_picker_nav"

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            textbutton _("Previous"):
                action FilePagePrevious()

            for i in range(1, 6):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

            textbutton _("  <<  "):
                action FilePageXtraPrevious()

            textbutton _("  >>  "):
                action FilePageXtraNext()

        $ columns = 2
        $ rows = 5

        grid columns rows:
            ypos 10
            transpose True
            xfill True
            style_group "file_picker"

            for i in range(1, columns * rows + 1):
                button:
                    xfill True
                    yfill True
                    xsize 490
                    ysize 75
                    padding(5,0)

                    if persistent.saveName:
                        action If(renpy.get_screen("save"), true=Show("savegameName", accept=FileSave(i)), false=FileLoad(i))
                    else:
                        action FileAction(i)

                    hbox:
                        add FileScreenshot(i) xalign 0.0

                        key "save_delete" action FileDelete(slot)

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)

                        if file_time == "Empty Slot.":
                            text "{b}[file_name]{/b}. [file_time!t]" xpos 0.35
                        else:
                            text "{b}[file_name]{/b}. [file_time!t]\n[save_name!t]" xoffset 50


screen save():
    tag menu
    use navigation
    use file_picker


screen load():
    tag menu
    use navigation
    use file_picker


screen delete():
    tag menu
    use navigation

    frame:
        yminimum 430
        style "file_picker_frame"

        has vbox

        hbox:
            xcenter 500
            style_group "file_picker_nav"
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 6):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

            textbutton _("  <<  "):
                action FilePageXtraPrevious()

            textbutton _("  >>  "):
                action FilePageXtraNext()

        $ columns = 2
        $ rows = 5

        grid columns rows:
            ypos 10
            transpose True
            xfill True
            style_group "file_picker"

            for i in range(1, columns * rows + 1):
                button:
                    action FileDelete(i)
                    xfill True
                    yfill True
                    xsize 490
                    ysize 75
                    padding (5,0)

                    has hbox

                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "{color=#870B0B}[file_name]. [file_time!t]\n[save_name!t]{/color}" xoffset 20

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


screen preferences():
    tag menu
    use navigation

    grid 3 1:
        style_group "prefs"
        xfill True

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

            frame:
                style_group "pref"
                has vbox

                label _("Language")
                textbutton "English" action Language(None), SetVariable("persistent.germanVariable", 0)

                textbutton "Deutsch" action Language("deutsch"), SetVariable("persistent.germanVariable", 1)

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"
            frame:
                style_group "pref"
                has vbox

                label _("Dialogue box opacity")
                bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider")

            frame:
                style_group "pref"
                has vbox
                label _("Save game names")
                style_prefix "radio"
                hbox:
                    textbutton _("Yes") action [SetVariable("persistent.saveName", True), SetVariable("store.save_name", "")]

                    textbutton _("No") action [SetVariable("persistent.saveName", False), SetVariable("store.save_name", "Un-Named")]

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


screen yesno_prompt(message, yes_action, no_action):
    modal True
    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


screen quick_menu():
    hbox:
        style_group "quick"
        xalign 1.0
        yalign 1.0

        if renpy.android:
            textbutton _("{color=#fff}Back{/color}      ") action Rollback() text_size 30
            textbutton _("{color=#fff}Skip{/color}    ") action Skip() text_size 30
            textbutton _("F.Skip      ") action Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
        else:
            textbutton _("{color=#fff}Back{/color}") action Rollback() text_size 15
            textbutton _("{color=#fff}Save{/color}") action ShowMenu('save') text_size 15
            textbutton _("{color=#fff}Skip{/color}") action Skip() text_size 15
            textbutton _("{color=#fff}F.Skip{/color}") action Skip(fast=True, confirm=True) text_size 15
            textbutton _("{color=#fff}Auto{/color}") action Preference("auto-forward", "toggle") text_size 15
            textbutton _("{color=#fff}Prefs{/color}") action ShowMenu('preferences') text_size 15

init -2:
    style quick_button is default:
        background None
        xpadding 5

    style quick_button_text is default:
        size 12
        idle_color "#8888"

        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


screen savegameName(accept=NullAction()):
    use navigation
    modal True
    add Solid("#000000") alpha 0.8
    style_prefix "savegameName"

    frame:
        has vbox
        xalign 0.5
        spacing 20

        label _("Save Name"):
            text_color "#fff"
            xalign 0.5

        null height 10

        input size 40 color "#fff" default store.save_name changed Namer length 70 allow allowedChars:
            yalign 1.0
            xalign 0.5
            xysize (550, 40)
        hbox:
            textbutton _("{b}Save Game{/b}"):
                keysym ['K_RETURN', 'K_KP_ENTER']
                action [accept, (Hide("savegameName"))]

            textbutton _("{b}Cancel{/b}"):
                action [Hide("savegameName"),ShowMenu('save')]


init:
    $ mupdate_counter = 0


init python:
    import string
    def Namer(name):
        store.save_name = name

define allowedChars = string.ascii_letters + string.digits + " -"
default persistent.saveName = False

style savegameName_frame:
    xsize 650
    xalign 0.5
    yalign 0.3

style savegameName_frame:
    variant "touch"
    xsize 650
    xalign 0.5
    yalign 0
    ypos 50


init -999 python:
    class FilePageXtraNext(Action, DictEquality):
        """
        :doc: file_action

        Goes to the next file page.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to.

        `wrap`
            If true, we can go to the first page when on the
            last file page if `max` is set.

        `auto`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.

        `quick`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.
        """
        
        alt = _("skip 50 slots")
        
        def __init__(self, max=None, wrap=False, auto=True, quick=True):
            
            page = persistent._file_page
            
            if page == "auto":
                if config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"
            
            elif page == "quick":
                page = "1"
            
            else:
                page = int(page) + 5
                
                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None
                
                if page is not None:
                    page = str(page)
            
            self.page = page
        
        def __call__(self):
            if not self.get_sensitive():
                return
            
            persistent._file_page = self.page
            renpy.restart_interaction()
        
        def get_sensitive(self):
            return self.page is not None
        
        def predict(self):
            _predict_file_page(self.page)


init -999 python:
    class FilePageXtraPrevious(Action, DictEquality):
        """
        :doc: file_action

        Goes to the next file page.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to.

        `wrap`
            If true, we can go to the first page when on the
            last file page if `max` is set.

        `auto`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.

        `quick`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.
        """
        
        alt = _("skip 50 slots")
        
        def __init__(self, max=None, wrap=False, auto=True, quick=True):
            
            page = persistent._file_page
            
            if page == "auto":
                if config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"
            
            elif page == "quick":
                page = "1"
            
            else:
                page = int(page) - 5
                if page <= 0:
                    page = 1
                
                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None
                
                if page is not None:
                    page = str(page)
            
            self.page = page
        
        def __call__(self):
            if not self.get_sensitive():
                return
            
            persistent._file_page = self.page
            renpy.restart_interaction()
        
        def get_sensitive(self):
            return self.page is not None
        
        def predict(self):
            _predict_file_page(self.page)

