
label main_menu:
    call screen main_menu
    return


label start:
    if start_search_menu:
        scene ingame_background
        show screen search_projects_menu

    if start_image_pos_tool:
        scene ingame_background
        show screen image_move_hidden
        show screen variable_monitoring

    # Here begins your game script.

    "line 1"
    "line 2"
    "line 3"
    "line 4"
    "line 5"
    "line 6"
    "line 7"
    "line 8"
    "line 9"
    "line 10"

    return

