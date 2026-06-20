
init:
    $ image_move_active = False
    $ file_location = ""
    $ layer = 0
    $ layers = []
    $ layer_loop = -1
    $ layer_loop1 = 0
    $ layer_loop2 = 0
    $ move_layers_simultan = False
    $ selected_layer = 0
    $ menu_extension = False
    $ text_show_var_scams = False
    $ rotate_range = 1
    $ zoom_range = 0.01
    $ xalign_range = 0.01
    $ yalign_range = 0.01
    $ zoom_var = 1.0
    $ show_saving = False
    $ current_directory = ""
    $ file_path = ""
    $ image_found = False

    $ h_flip = False
    $ v_flip = False
    $ xzoom_var = 0.0
    $ yzoom_var = 0.0
    $ xalign_var = 0.50
    $ yalign_var = 0.50
    $ rotate_var = 0

    $ layer1_active = False
    $ xzoom_var1 = 0.0
    $ yzoom_var1 = 0.0
    $ xalign_var1 = 0.50
    $ yalign_var1 = 0.50
    $ rotate_var1 = 0
    $ h_flip_var1 = False
    $ v_flip_var1 = False

    $ layer2_active = False
    $ xzoom_var2 = 0.0
    $ yzoom_var2 = 0.0
    $ xalign_var2 = 0.50
    $ yalign_var2 = 0.50
    $ rotate_var2 = 0
    $ diff_rotate_var2 = 0
    $ diff_xalign_var2 = 0
    $ diff_yalign_var2 = 0
    $ h_flip_var2 = False
    $ v_flip_var2 = False

    $ layer3_active = False
    $ xzoom_var3 = 0.0
    $ yzoom_var3 = 0.0
    $ xalign_var3 = 0.50
    $ yalign_var3 = 0.50
    $ rotate_var3 = 0
    $ diff_rotate_var3 = 0
    $ diff_xalign_var3 = 0
    $ diff_yalign_var3 = 0
    $ h_flip_var3 = False
    $ v_flip_var3 = False

    $ layer4_active = False
    $ xzoom_var4 = 0.0
    $ yzoom_var4 = 0.0
    $ xalign_var4 = 0.50
    $ yalign_var4 = 0.50
    $ rotate_var4 = 0
    $ diff_rotate_var4 = 0
    $ diff_xalign_var4 = 0
    $ diff_yalign_var4 = 0
    $ h_flip_var4 = False
    $ v_flip_var4 = False

    $ layer5_active = False
    $ xzoom_var5 = 0.0
    $ yzoom_var5 = 0.0
    $ xalign_var5 = 0.50
    $ yalign_var5 = 0.50
    $ rotate_var5 = 0
    $ diff_rotate_var5 = 0
    $ diff_xalign_var5 = 0
    $ diff_yalign_var5 = 0
    $ h_flip_var5 = False
    $ v_flip_var5 = False

    $ layer6_active = False
    $ xzoom_var6 = 0.0
    $ yzoom_var6 = 0.0
    $ xalign_var6 = 0.50
    $ yalign_var6 = 0.50
    $ rotate_var6 = 0
    $ diff_rotate_var6 = 0
    $ diff_xalign_var6 = 0
    $ diff_yalign_var6 = 0
    $ h_flip_var6 = False
    $ v_flip_var6 = False

    $ layer7_active = False
    $ xzoom_var7 = 0.0
    $ yzoom_var7 = 0.0
    $ xalign_var7 = 0.50
    $ yalign_var7 = 0.50
    $ rotate_var7 = 0
    $ diff_rotate_var7 = 0
    $ diff_xalign_var7 = 0
    $ diff_yalign_var7 = 0
    $ h_flip_var7 = False
    $ v_flip_var7 = False

    $ layer8_active = False
    $ xzoom_var8 = 0.0
    $ yzoom_var8 = 0.0
    $ xalign_var8 = 0.50
    $ yalign_var8 = 0.50
    $ rotate_var8 = 0
    $ diff_rotate_var8 = 0
    $ diff_xalign_var8 = 0
    $ diff_yalign_var8 = 0
    $ h_flip_var8 = False
    $ v_flip_var8 = False

    $ layer9_active = False
    $ xzoom_var9 = 0.0
    $ yzoom_var9 = 0.0
    $ xalign_var9 = 0.50
    $ yalign_var9 = 0.50
    $ rotate_var9 = 0
    $ diff_rotate_var9 = 0
    $ diff_xalign_var9 = 0
    $ diff_yalign_var9 = 0
    $ h_flip_var9 = False
    $ v_flip_var9 = False

    $ layer10_active = False
    $ xzoom_var10 = 0.0
    $ yzoom_var10 = 0.0
    $ xalign_var10 = 0.50
    $ yalign_var10 = 0.50
    $ rotate_var10 = 0
    $ diff_rotate_var10 = 0
    $ diff_xalign_var10 = 0
    $ diff_yalign_var10 = 0
    $ h_flip_var10 = False
    $ v_flip_var10 = False

    $ layer11_active = False
    $ xzoom_var11 = 0.0
    $ yzoom_var11 = 0.0
    $ xalign_var11 = 0.50
    $ yalign_var11 = 0.50
    $ rotate_var11 = 0
    $ diff_rotate_var11 = 0
    $ diff_xalign_var11 = 0
    $ diff_yalign_var11 = 0
    $ h_flip_var11 = False
    $ v_flip_var11 = False

    $ layer12_active = False
    $ xzoom_var12 = 0.0
    $ yzoom_var12 = 0.0
    $ xalign_var12 = 0.50
    $ yalign_var12 = 0.50
    $ rotate_var12 = 0
    $ diff_rotate_var12 = 0
    $ diff_xalign_var12 = 0
    $ diff_yalign_var12 = 0
    $ h_flip_var12 = False
    $ v_flip_var12 = False

    $ layer13_active = False
    $ xzoom_var13 = 0.0
    $ yzoom_var13 = 0.0
    $ xalign_var13 = 0.50
    $ yalign_var13 = 0.50
    $ rotate_var13 = 0
    $ diff_rotate_var13 = 0
    $ diff_xalign_var13 = 0
    $ diff_yalign_var13 = 0
    $ h_flip_var13 = False
    $ v_flip_var13 = False

    $ layer14_active = False
    $ xzoom_var14 = 0.0
    $ yzoom_var14 = 0.0
    $ xalign_var14 = 0.50
    $ yalign_var14 = 0.50
    $ rotate_var14 = 0
    $ diff_rotate_var14 = 0
    $ diff_xalign_var14 = 0
    $ diff_yalign_var14 = 0
    $ h_flip_var14 = False
    $ v_flip_var14 = False

    $ layer15_active = False
    $ xzoom_var15 = 0.0
    $ yzoom_var15 = 0.0
    $ xalign_var15 = 0.50
    $ yalign_var15 = 0.50
    $ rotate_var15 = 0
    $ diff_rotate_var15 = 0
    $ diff_xalign_var15 = 0
    $ diff_yalign_var15 = 0
    $ h_flip_var15 = False
    $ v_flip_var15 = False

    $ layer16_active = False
    $ xzoom_var16 = 0.0
    $ yzoom_var16 = 0.0
    $ xalign_var16 = 0.50
    $ yalign_var16 = 0.50
    $ rotate_var16 = 0
    $ diff_rotate_var16 = 0
    $ diff_xalign_var16 = 0
    $ diff_yalign_var16 = 0
    $ h_flip_var16 = False
    $ v_flip_var16 = False

    $ layer17_active = False
    $ xzoom_var17 = 0.0
    $ yzoom_var17 = 0.0
    $ xalign_var17 = 0.50
    $ yalign_var17 = 0.50
    $ rotate_var17 = 0
    $ diff_rotate_var17 = 0
    $ diff_xalign_var17 = 0
    $ diff_yalign_var17 = 0
    $ h_flip_var17 = False
    $ v_flip_var17 = False

    $ layer18_active = False
    $ xzoom_var18 = 0.0
    $ yzoom_var18 = 0.0
    $ xalign_var18 = 0.50
    $ yalign_var18 = 0.50
    $ rotate_var18 = 0
    $ diff_rotate_var18 = 0
    $ diff_xalign_var18 = 0
    $ diff_yalign_var18 = 0
    $ h_flip_var18 = False
    $ v_flip_var18 = False

    $ layer19_active = False
    $ xzoom_var19 = 0.0
    $ yzoom_var19 = 0.0
    $ xalign_var19 = 0.50
    $ yalign_var19 = 0.50
    $ rotate_var19 = 0
    $ diff_rotate_var19 = 0
    $ diff_xalign_var19 = 0
    $ diff_yalign_var19 = 0
    $ h_flip_var19 = False
    $ v_flip_var19 = False

    $ layer20_active = False
    $ xzoom_var20 = 0.0
    $ yzoom_var20 = 0.0
    $ xalign_var20 = 0.50
    $ yalign_var20 = 0.50
    $ rotate_var20 = 0
    $ diff_rotate_var20 = 0
    $ diff_xalign_var20 = 0
    $ diff_yalign_var20 = 0
    $ h_flip_var20 = False
    $ v_flip_var20 = False

    $ layer21_active = False
    $ xzoom_var21 = 0.0
    $ yzoom_var21 = 0.0
    $ xalign_var21 = 0.50
    $ yalign_var21 = 0.50
    $ rotate_var21 = 0
    $ diff_rotate_var21 = 0
    $ diff_xalign_var21 = 0
    $ diff_yalign_var21 = 0
    $ h_flip_var21 = False
    $ v_flip_var21 = False

    $ layer22_active = False
    $ xzoom_var22 = 0.0
    $ yzoom_var22 = 0.0
    $ xalign_var22 = 0.50
    $ yalign_var22 = 0.50
    $ rotate_var22 = 0
    $ diff_rotate_var22 = 0
    $ diff_xalign_var22 = 0
    $ diff_yalign_var22 = 0
    $ h_flip_var22 = False
    $ v_flip_var22 = False

    $ layer23_active = False
    $ xzoom_var23 = 0.0
    $ yzoom_var23 = 0.0
    $ xalign_var23 = 0.50
    $ yalign_var23 = 0.50
    $ rotate_var23 = 0
    $ diff_rotate_var23 = 0
    $ diff_xalign_var23 = 0
    $ diff_yalign_var23 = 0
    $ h_flip_var23 = False
    $ v_flip_var23 = False

    $ layer24_active = False
    $ xzoom_var24 = 0.0
    $ yzoom_var24 = 0.0
    $ xalign_var24 = 0.50
    $ yalign_var24 = 0.50
    $ rotate_var24 = 0
    $ diff_rotate_var24 = 0
    $ diff_xalign_var24 = 0
    $ diff_yalign_var24 = 0
    $ h_flip_var24 = False
    $ v_flip_var24 = False

    $ layer25_active = False
    $ xzoom_var25 = 0.0
    $ yzoom_var25 = 0.0
    $ xalign_var25 = 0.50
    $ yalign_var25 = 0.50
    $ rotate_var25 = 0
    $ diff_rotate_var25 = 0
    $ diff_xalign_var25 = 0
    $ diff_yalign_var25 = 0
    $ h_flip_var25 = False
    $ v_flip_var25 = False

    $ layer26_active = False
    $ xzoom_var26 = 0.0
    $ yzoom_var26 = 0.0
    $ xalign_var26 = 0.50
    $ yalign_var26 = 0.50
    $ rotate_var26 = 0
    $ diff_rotate_var26 = 0
    $ diff_xalign_var26 = 0
    $ diff_yalign_var26 = 0
    $ h_flip_var26 = False
    $ v_flip_var26 = False

    $ layer27_active = False
    $ xzoom_var27 = 0.0
    $ yzoom_var27 = 0.0
    $ xalign_var27 = 0.50
    $ yalign_var27 = 0.50
    $ rotate_var27 = 0
    $ diff_rotate_var27 = 0
    $ diff_xalign_var27 = 0
    $ diff_yalign_var27 = 0
    $ h_flip_var27 = False
    $ v_flip_var27 = False

    $ layer28_active = False
    $ xzoom_var28 = 0.0
    $ yzoom_var28 = 0.0
    $ xalign_var28 = 0.50
    $ yalign_var28 = 0.50
    $ rotate_var28 = 0
    $ diff_rotate_var28 = 0
    $ diff_xalign_var28 = 0
    $ diff_yalign_var28 = 0
    $ h_flip_var28 = False
    $ v_flip_var28 = False

    $ layer29_active = False
    $ xzoom_var29 = 0.0
    $ yzoom_var29 = 0.0
    $ xalign_var29 = 0.50
    $ yalign_var29 = 0.50
    $ rotate_var29 = 0
    $ diff_rotate_var29 = 0
    $ diff_xalign_var29 = 0
    $ diff_yalign_var29 = 0
    $ h_flip_var29 = False
    $ v_flip_var29 = False

    $ layer30_active = False
    $ xzoom_var30 = 0.0
    $ yzoom_var30 = 0.0
    $ xalign_var30 = 0.50
    $ yalign_var30 = 0.50
    $ rotate_var30 = 0
    $ diff_rotate_var30 = 0
    $ diff_xalign_var30 = 0
    $ diff_yalign_var30 = 0
    $ h_flip_var30 = False
    $ v_flip_var30 = False

init python:
    from datetime import datetime


screen locationput(prompt):
    frame:
        ypos 416 xsize 412 ysize 200
        has vbox
        xoffset 5
        yoffset 0
        text prompt style "input_prompt"
        input id "input" style "input_text" color "#ffffff"
        textbutton "{color=#4f7649}return" action Jump("image_loop") xpos 315 ypos 70 text_size 16


screen message_delete_layers():
    frame:
        ypos 416 xsize 412 ysize 100
        vbox:
            textbutton "{color=#cb1e1e}Maximum number of layers reached." xsize 400 text_size 16
            textbutton "{color=#cb1e1e}Please delete the current image." xsize 400 text_size 16
        textbutton "{color=#4f7649}return" action Hide("message_delete_layers"), SetVariable("image_found", False), Jump("image_loop") at right text_size 16


screen image_loading_error():
    frame:
        ypos 416 xsize 412 ysize 125
        vbox:
            label "{color=#cb1e1e}Image file not found." xsize 400 text_size 16
            label "{color=#cb1e1e}\nPlease enter the correct folder path and the file name, including the file extension." xsize 400 text_size 16
            textbutton "{color=#4f7649}return" action Hide("image_loading_error") xpos 315 ypos 20 text_size 16


screen delete_query():
    frame:
        ypos 416 xsize 412 ysize 100
        vbox:
            label "{color=#cb1e1e}Are you sure you want to delete all layers?" xsize 400 text_size 16
        hbox:
            textbutton "{color=#cb1e1e}Yes" xpos 85 ypos 40 xsize 50 text_size 16 action Hide("delete_query"), Call("delete_image_move")
            textbutton "{color=#238626}No" xpos 200 ypos 40 xsize 50 text_size 16 action Hide("delete_query"), Jump("image_loop")


screen image_move():
    frame:
        has hbox
        vbox:
            if selected_layer != 0 or (move_layers_simultan and layer > 0):
                textbutton "rotate left ( {b}[rotate_var]{/b} )" action SetVariable("rotate_var", rotate_var - rotate_range), Jump("restart_image") xsize 200 text_size 16
                textbutton "rotate right ( {b}[rotate_var]{/b} )" action SetVariable("rotate_var", rotate_var + rotate_range), Jump("restart_image") xsize 200 text_size 16

                if not move_layers_simultan:
                    textbutton "zoom +   ( {b}[zoom_var:.2f]{/b} )" action SetVariable("zoom_var", zoom_var + zoom_range), Jump("restart_image") xsize 200 text_size 16
                if move_layers_simultan:
                    textbutton "zoom +   ( {b}[zoom_var:.2f]{/b} )" xsize 200 text_size 16
                if not move_layers_simultan:
                    textbutton "zoom -   ( {b}[zoom_var:.2f]{/b} )" action SetVariable("zoom_var", zoom_var - zoom_range), Jump("restart_image") xsize 200 text_size 16
                if move_layers_simultan:
                    textbutton "zoom -   ( {b}[zoom_var:.2f]{/b} )" xsize 200 text_size 16

                textbutton "xalign +   ( {b}[xalign_var:.2f]{/b} )" action SetVariable("xalign_var", xalign_var + xalign_range), Jump("restart_image") xsize 200 text_size 16
                textbutton "xalign -   ( {b}[xalign_var:.2f]{/b} )" action SetVariable("xalign_var", xalign_var - xalign_range), Jump("restart_image") xsize 200 text_size 16

                textbutton "yalign +   ( {b}[yalign_var:.2f]{/b} )" action SetVariable("yalign_var", yalign_var + yalign_range), Jump("restart_image") xsize 200 text_size 16
                textbutton "yalign -   ( {b}[yalign_var:.2f]{/b} )" action SetVariable("yalign_var", yalign_var - yalign_range), Jump("restart_image") xsize 200 text_size 16

            if selected_layer == 0 or (move_layers_simultan and layer == 0):
                textbutton "rotate left ( {b}[rotate_var]{/b} )" xsize 200 text_size 16
                textbutton "rotate right ( {b}[rotate_var]{/b} )" xsize 200 text_size 16
                textbutton "zoom +   ( {b}[zoom_var:.2f]{/b} )" xsize 200 text_size 16
                textbutton "zoom -   ( {b}[zoom_var:.2f]{/b} )" xsize 200 text_size 16
                textbutton "xalign +   ( {b}[xalign_var:.2f]{/b} )" xsize 200 text_size 16
                textbutton "xalign -   ( {b}[xalign_var:.2f]{/b} )" xsize 200 text_size 16
                textbutton "yalign +   ( {b}[yalign_var:.2f]{/b} )" xsize 200 text_size 16
                textbutton "yalign -   ( {b}[yalign_var:.2f]{/b} )" xsize 200 text_size 16

        vbox:
            textbutton " + " action SetVariable("rotate_range", rotate_range + 1) xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " + " action SetVariable("zoom_range", zoom_range + 0.01) xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " + " action SetVariable("xalign_range", xalign_range + 0.01) xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " + " action SetVariable("yalign_range", yalign_range + 0.01) xsize 30 text_size 16
            label "" xsize 30 text_size 16

        vbox:
            textbutton " rotate_range: {b}[rotate_range]{/b}" action Jump("input_rotate") xsize 140 text_size 16
            textbutton " zoom_range: {b}[zoom_range:.2f]{/b}" action Jump("input_zoom") xsize 140 text_size 16
            textbutton " xalign_range: {b}[xalign_range:.2f]{/b}" action Jump("input_xalign") xsize 140 text_size 16
            textbutton " yalign_range: {b}[yalign_range:.2f]{/b}" action Jump("input_yalign") xsize 140 text_size 16

            hbox:
                if selected_layer != 0:
                    if ((selected_layer == 1 and h_flip_var1) or
                        (selected_layer == 2 and h_flip_var2) or
                        (selected_layer == 3 and h_flip_var3) or
                        (selected_layer == 4 and h_flip_var4) or
                        (selected_layer == 5 and h_flip_var5) or
                        (selected_layer == 6 and h_flip_var6) or
                        (selected_layer == 7 and h_flip_var7) or
                        (selected_layer == 8 and h_flip_var8) or
                        (selected_layer == 9 and h_flip_var9) or
                        (selected_layer == 10 and h_flip_var10) or
                        (selected_layer == 11 and h_flip_var11) or
                        (selected_layer == 12 and h_flip_var12) or
                        (selected_layer == 13 and h_flip_var13) or
                        (selected_layer == 14 and h_flip_var14) or
                        (selected_layer == 15 and h_flip_var15) or
                        (selected_layer == 16 and h_flip_var16) or
                        (selected_layer == 17 and h_flip_var17) or
                        (selected_layer == 18 and h_flip_var18) or
                        (selected_layer == 19 and h_flip_var19) or
                        (selected_layer == 20 and h_flip_var20) or
                        (selected_layer == 21 and h_flip_var21) or
                        (selected_layer == 22 and h_flip_var22) or
                        (selected_layer == 23 and h_flip_var23) or
                        (selected_layer == 24 and h_flip_var24) or
                        (selected_layer == 25 and h_flip_var25) or
                        (selected_layer == 26 and h_flip_var26) or
                        (selected_layer == 27 and h_flip_var27) or
                        (selected_layer == 28 and h_flip_var28) or
                        (selected_layer == 29 and h_flip_var29) or
                        (selected_layer == 30 and h_flip_var30)) and not move_layers_simultan:
                        $ h_flip = True
                        textbutton "{color=#cb1e1e}Flip H" action SetVariable("h_flip", False), Jump("restart_image") xsize 70 text_size 14

                    if not ((selected_layer == 1 and h_flip_var1) or
                            (selected_layer == 2 and h_flip_var2) or
                            (selected_layer == 3 and h_flip_var3) or
                            (selected_layer == 4 and h_flip_var4) or
                            (selected_layer == 5 and h_flip_var5) or
                            (selected_layer == 6 and h_flip_var6) or
                            (selected_layer == 7 and h_flip_var7) or
                            (selected_layer == 8 and h_flip_var8) or
                            (selected_layer == 9 and h_flip_var9) or
                            (selected_layer == 10 and h_flip_var10) or
                            (selected_layer == 11 and h_flip_var11) or
                            (selected_layer == 12 and h_flip_var12) or
                            (selected_layer == 13 and h_flip_var13) or
                            (selected_layer == 14 and h_flip_var14) or
                            (selected_layer == 15 and h_flip_var15) or
                            (selected_layer == 16 and h_flip_var16) or
                            (selected_layer == 17 and h_flip_var17) or
                            (selected_layer == 18 and h_flip_var18) or
                            (selected_layer == 19 and h_flip_var19) or
                            (selected_layer == 20 and h_flip_var20) or
                            (selected_layer == 21 and h_flip_var21) or
                            (selected_layer == 22 and h_flip_var22) or
                            (selected_layer == 23 and h_flip_var23) or
                            (selected_layer == 24 and h_flip_var24) or
                            (selected_layer == 25 and h_flip_var25) or
                            (selected_layer == 26 and h_flip_var26) or
                            (selected_layer == 27 and h_flip_var27) or
                            (selected_layer == 28 and h_flip_var28) or
                            (selected_layer == 29 and h_flip_var29) or
                            (selected_layer == 30 and h_flip_var30)) and not move_layers_simultan:
                            $ h_flip = False
                            textbutton "Flip H" action SetVariable("h_flip", True), Jump("restart_image") xsize 70 text_size 14

                    if ((selected_layer == 1 and v_flip_var1) or
                        (selected_layer == 2 and v_flip_var2) or
                        (selected_layer == 3 and v_flip_var3) or
                        (selected_layer == 4 and v_flip_var4) or
                        (selected_layer == 5 and v_flip_var5) or
                        (selected_layer == 6 and v_flip_var6) or
                        (selected_layer == 7 and v_flip_var7) or
                        (selected_layer == 8 and v_flip_var8) or
                        (selected_layer == 9 and v_flip_var9) or
                        (selected_layer == 10 and v_flip_var10) or
                        (selected_layer == 11 and v_flip_var11) or
                        (selected_layer == 12 and v_flip_var12) or
                        (selected_layer == 13 and v_flip_var13) or
                        (selected_layer == 14 and v_flip_var14) or
                        (selected_layer == 15 and v_flip_var15) or
                        (selected_layer == 16 and v_flip_var16) or
                        (selected_layer == 17 and v_flip_var17) or
                        (selected_layer == 18 and v_flip_var18) or
                        (selected_layer == 19 and v_flip_var19) or
                        (selected_layer == 20 and v_flip_var20) or
                        (selected_layer == 21 and v_flip_var21) or
                        (selected_layer == 22 and v_flip_var22) or
                        (selected_layer == 23 and v_flip_var23) or
                        (selected_layer == 24 and v_flip_var24) or
                        (selected_layer == 25 and v_flip_var25) or
                        (selected_layer == 26 and v_flip_var26) or
                        (selected_layer == 27 and v_flip_var27) or
                        (selected_layer == 28 and v_flip_var28) or
                        (selected_layer == 29 and v_flip_var29) or
                        (selected_layer == 30 and v_flip_var30)) and not move_layers_simultan:
                        $ v_flip = True
                        textbutton "{color=#cb1e1e}Flip V" action SetVariable("v_flip", False), Jump("restart_image") xsize 70 text_size 14

                    if not ((selected_layer == 1 and v_flip_var1) or
                            (selected_layer == 2 and v_flip_var2) or
                            (selected_layer == 3 and v_flip_var3) or
                            (selected_layer == 4 and v_flip_var4) or
                            (selected_layer == 5 and v_flip_var5) or
                            (selected_layer == 6 and v_flip_var6) or
                            (selected_layer == 7 and v_flip_var7) or
                            (selected_layer == 8 and v_flip_var8) or
                            (selected_layer == 9 and v_flip_var9) or
                            (selected_layer == 10 and v_flip_var10) or
                            (selected_layer == 11 and v_flip_var11) or
                            (selected_layer == 12 and v_flip_var12) or
                            (selected_layer == 13 and v_flip_var13) or
                            (selected_layer == 14 and v_flip_var14) or
                            (selected_layer == 15 and v_flip_var15) or
                            (selected_layer == 16 and v_flip_var16) or
                            (selected_layer == 17 and v_flip_var17) or
                            (selected_layer == 18 and v_flip_var18) or
                            (selected_layer == 19 and v_flip_var19) or
                            (selected_layer == 20 and v_flip_var20) or
                            (selected_layer == 21 and v_flip_var21) or
                            (selected_layer == 22 and v_flip_var22) or
                            (selected_layer == 23 and v_flip_var23) or
                            (selected_layer == 24 and v_flip_var24) or
                            (selected_layer == 25 and v_flip_var25) or
                            (selected_layer == 26 and v_flip_var26) or
                            (selected_layer == 27 and v_flip_var27) or
                            (selected_layer == 28 and v_flip_var28) or
                            (selected_layer == 29 and v_flip_var29) or
                            (selected_layer == 30 and v_flip_var30)) and not move_layers_simultan:
                        $ v_flip = False
                        textbutton "Flip V" action SetVariable("v_flip", True), Jump("restart_image") xsize 70 text_size 14

                if selected_layer == 0 or move_layers_simultan:
                    textbutton "Flip H" xsize 70 text_size 14
                    textbutton "Flip V" xsize 70 text_size 14

        vbox:
            textbutton " - " action SetVariable("rotate_range", rotate_range - 1), Jump("image_loop") xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " - " action SetVariable("zoom_range", zoom_range - 0.01), Jump("image_loop") xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " - " action SetVariable("xalign_range", xalign_range - 0.01), Jump("image_loop") xsize 30 text_size 16
            label "" xsize 30 text_size 16
            textbutton " - " action SetVariable("yalign_range", yalign_range - 0.01), Jump("image_loop") xsize 30 text_size 16
            label "" xsize 30 text_size 16

    frame:
        ypos 192 xsize 412
        vbox:
            label "Maximum number of layers: 30" text_size 16 at center
            label "Number of active layers: [layer]" text_size 16 at center

            if move_layers_simultan:
                textbutton "{color=#4f7649}Move layers simultaneously: on" action SetVariable("move_layers_simultan", False), SetVariable("selected_layer", 1) xsize 400 text_size 16
                textbutton "Move layers individually: off" xsize 400 text_size 16
            if not move_layers_simultan:
                textbutton "Move layers simultaneously: off" xsize 400 text_size 16
                textbutton "{color=#4f7649}Move layers individually: on" action SetVariable("move_layers_simultan", True), SetVariable("rotate_var", rotate_var1), SetVariable("xalign_var", xalign_var1), SetVariable("yalign_var", yalign_var1), Hide("image_loading_error"), SetVariable("image_found", False), Jump("layer_diff") xsize 400 text_size 16

            if layer > 0 and not move_layers_simultan:
                textbutton "{color=#4f7649}Selected Layer: [selected_layer]" action SetVariable("selected_layer", selected_layer + 1), Hide("image_loading_error"), SetVariable("image_found", False), Jump("restart_layer_counter") xsize 400 text_size 16
            if layer == 0 and not move_layers_simultan:
                textbutton "No layer selected" xsize 400 text_size 16

            if move_layers_simultan:
                textbutton "All Layers Selected" xsize 400 text_size 16
                textbutton "Input File Location" xsize 400 text_size 16
            if not move_layers_simultan:
                textbutton "{color=#4f7649}Input File Location" action Hide("image_loading_error"), SetVariable("image_found", False), Call("input_image") xsize 400 text_size 16

            if layer > 0:
                textbutton "{color=#4f7649}Delete Image" action Hide("image_loading_error"), Hide("message_delete_layers"), SetVariable("image_found", False), Show("delete_query") xsize 400 text_size 16
            if layer == 0:
                textbutton "Delete Image" xsize 400 text_size 16

            if image_move_active:
                textbutton "{color=#4f7649}Return / {color=#cb1e1e}Continue Game{/color}" action Hide("image_loading_error"), SetVariable("image_found", False), SetVariable("image_move_active", False), Jump("continue_game") xsize 400 text_size 16
            if not image_move_active:
                textbutton "{color=#4f7649}Return" action Hide("image_loading_error"), SetVariable("image_move_active", False), SetVariable("image_found", False), Jump("continue_game") xsize 400 text_size 16

            if not show_saving:
                textbutton "Save Layer Data in \"layer_positions.txt\"" action SetVariable("show_saving", True), Call("save_layer_data") xsize 400 text_size 16
            if show_saving:
                textbutton "{color=#cb1e1e}Save Layer Data...{/color}" xsize 400 text_size 16
                timer 1.5 action SetVariable("show_saving", False), Jump("image_loop")

            textbutton "{color=#4f7649}Hide Current Menu" action Hide("image_loading_error"), SetVariable("image_move_active", False), Hide("image_move", transition = Dissolve(0.2)), Hide("message_delete_layers", transition = Dissolve(0.2)), Hide("locationput", transition = Dissolve(0.2)), Hide("", transition = Dissolve(0.2)), Show("image_move_hidden", transition = Dissolve(0.2)) xsize 400 text_size 16


screen image_move_hidden():
    textbutton "Show Image Move Menu" action Hide("image_move_hidden", transition = Dissolve(0.2)), Show("image_move", transition = Dissolve(0.2)) text_size 12


screen variable_monitoring():
    frame at right:
        background Frame(Transform("#77c966", alpha = persistent.dialogueBoxOpacity))
        text "{color=#000000}h_flip = {color=#ac1111}[h_flip]\n{color=#000000}h_flip_var1 = {color=#ac1111}[h_flip_var1]\n{color=#000000}h_flip_var2 = {color=#ac1111}[h_flip_var2]\n{color=#000000}h_flip_var3 = {color=#ac1111}[h_flip_var3]\n{color=#000000}h_flip_var4 = {color=#ac1111}[h_flip_var4]\n{color=#000000}h_flip_var5 = {color=#ac1111}[h_flip_var5]\n{color=#000000}h_flip_var6 = {color=#ac1111}[h_flip_var6]\n{color=#000000}v_flip = {color=#ac1111}[v_flip]\n{color=#000000}v_flip_var1 = {color=#ac1111}[v_flip_var1]\n{color=#000000}v_flip_var2 = {color=#ac1111}[v_flip_var2]\n{color=#000000}v_flip_var3 = {color=#ac1111}[v_flip_var3]\n{color=#000000}v_flip_var4 = {color=#ac1111}[v_flip_var4]\n{color=#000000}v_flip_var5 = {color=#ac1111}[v_flip_var5]\n{color=#000000}v_flip_var6 = {color=#ac1111}[v_flip_var6]\n{color=#000000}move_layers_simultan = {color=#ac1111}[move_layers_simultan]" size 12

# \n{color=#000000} = {color=#ac1111}[]


label list_image_files:
    python:
        image_dir = "images/"
        for image_list in renpy.list_files():
            if image_list.startswith(image_dir):
                if file_location == image_list:
                    image_found = True
        image_png_found = False
        image_jpg_found = False
        image_jpeg_found = False
        image_webp_found = False
        image_avif_found = False
        image_svg_found = False
        if image_found:
            renpy.jump("load_image")
        else:
            layer -= 1
            selected_layer -= 1
            renpy.show_screen("image_loading_error")
            renpy.pause(hard = True)


label input_image:
    if layer == 30:
        show screen message_delete_layers
        jump image_loop
    $ location_input = renpy.input("{size=-1}{color=#4f7649}\nEnter folder path and file name: \n{/color}{/size}", exclude = '{}', length = 30, with_none = None, pixel_width = None, screen = 'locationput', default = 'images/', allow = None)
    if location_input == "":
        jump image_loop
    if layer < 30:
        $ layer += 1
    if layer == 0:
        $ selected_layer = 0
    if layer == 1:
        $ selected_layer = 1
    if layer == 2:
        $ selected_layer = 2
    if layer == 3:
        $ selected_layer = 3
    if layer == 4:
        $ selected_layer = 4
    if layer == 5:
        $ selected_layer = 5
    if layer == 6:
        $ selected_layer = 6
    if layer == 7:
        $ selected_layer = 7
    if layer == 8:
        $ selected_layer = 8
    if layer == 9:
        $ selected_layer = 9
    if layer == 10:
        $ selected_layer = 10
    if layer == 11:
        $ selected_layer = 11
    if layer == 12:
        $ selected_layer = 12
    if layer == 13:
        $ selected_layer = 13
    if layer == 14:
        $ selected_layer = 14
    if layer == 15:
        $ selected_layer = 15
    if layer == 16:
        $ selected_layer = 16
    if layer == 17:
        $ selected_layer = 17
    if layer == 18:
        $ selected_layer = 18
    if layer == 19:
        $ selected_layer = 19
    if layer == 20:
        $ selected_layer = 20
    if layer == 21:
        $ selected_layer = 21
    if layer == 22:
        $ selected_layer = 22
    if layer == 23:
        $ selected_layer = 23
    if layer == 24:
        $ selected_layer = 24
    if layer == 25:
        $ selected_layer = 25
    if layer == 26:
        $ selected_layer = 26
    if layer == 27:
        $ selected_layer = 27
    if layer == 28:
        $ selected_layer = 28
    if layer == 29:
        $ selected_layer = 29
    if layer == 30:
        $ selected_layer = 30
    $ file_location = location_input
    $ h_flip = False
    $ v_flip = False
    jump list_image_files


label input_rotate:
    $ rotate_input = renpy.input("{size=-5}{color=#fff}Rotate_range: {/color}{/size}", exclude='{}', length=3, with_none=None, pixel_width=None, screen='locationput')
    if rotate_input == "":
        $ rotate_input = "0"
    $ rotate_range = int(rotate_input)
    jump image_loop


label input_zoom:
    $ zoom_input = renpy.input("{size=-5}{color=#fff}Zoom_range: {/color}{/size}", exclude='{}', length=4, with_none=None, pixel_width=None, screen='locationput', allow = "0,1,2,3,4,5,6,7,8,9,.")
    if zoom_input == "":
        $ zoom_input = "0.00"
    $ zoom_range = float(zoom_input)
    jump image_loop


label input_xalign:
    $ xalign_input = renpy.input("{size=-5}{color=#fff}Zoom_range: {/color}{/size}", exclude='{}', length=4, with_none=None, pixel_width=None, screen='locationput', allow = "0,1,2,3,4,5,6,7,8,9,.")
    if xalign_input == "":
        $ xalign_input = "0.00"
    $ xalign_range = float(xalign_input)
    jump image_loop


label input_yalign:
    $ yalign_input = renpy.input("{size=-5}{color=#fff}Zoom_range: {/color}{/size}", exclude='{}', length=4, with_none=None, pixel_width=None, screen='locationput', allow = "0,1,2,3,4,5,6,7,8,9,.")
    if yalign_input == "":
        $ yalign_input = "0.00"
    $ yalign_range = float(yalign_input)
    jump image_loop


label image_loop:
    $ image_move_active = True
    if rotate_range < 0:
        $ rotate_range = 0
    if zoom_range < 0:
        $ zoom_range = 0.00
    if xalign_range < 0:
        $ xalign_range = 0.00
    if yalign_range < 0:
        $ yalign_range = 0.00
    hide screen image_move
    show screen image_move
    $ renpy.pause(hard=True)


label load_image:
    if not move_layers_simultan:

        if layer == 1 and not layer1_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer1_active = True
            if h_flip:
                $ xzoom_var1 = zoom_var * -1
            if not h_flip:
                $ xzoom_var1 = zoom_var
            if v_flip:
                $ yzoom_var1 = zoom_var * -1
            if not v_flip:
                $ yzoom_var1 = zoom_var
            $ rotate_var1 = rotate_var
            $ xalign_var1 = xalign_var
            $ yalign_var1 = yalign_var
            $ image_found = False
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1

        if layer == 2 and not layer2_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer2_active = True
            if h_flip:
                $ xzoom_var2 = zoom_var * -1
            if not h_flip:
                $ xzoom_var2 = zoom_var
            if v_flip:
                $ yzoom_var2 = zoom_var * -1
            if not v_flip:
                $ yzoom_var2 = zoom_var
            $ rotate_var2 = rotate_var
            $ xalign_var2 = xalign_var
            $ yalign_var2 = yalign_var
            $ image_found = False
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2

        if layer == 3 and not layer3_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer3_active = True
            if h_flip:
                $ xzoom_var3 = zoom_var * -1
            if not h_flip:
                $ xzoom_var3 = zoom_var
            if v_flip:
                $ yzoom_var3 = zoom_var * -1
            if not v_flip:
                $ yzoom_var3 = zoom_var
            $ rotate_var3 = rotate_var
            $ xalign_var3 = xalign_var
            $ yalign_var3 = yalign_var
            $ image_found = False
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3

        if layer == 4 and not layer4_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer4_active = True
            if h_flip:
                $ xzoom_var4 = zoom_var * -1
            if not h_flip:
                $ xzoom_var4 = zoom_var
            if v_flip:
                $ yzoom_var4 = zoom_var * -1
            if not v_flip:
                $ yzoom_var4 = zoom_var
            $ rotate_var4 = rotate_var
            $ xalign_var4 = xalign_var
            $ yalign_var4 = yalign_var
            $ image_found = False
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4

        if layer == 5 and not layer5_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer5_active = True
            if h_flip:
                $ xzoom_var5 = zoom_var * -1
            if not h_flip:
                $ xzoom_var5 = zoom_var
            if v_flip:
                $ yzoom_var5 = zoom_var * -1
            if not v_flip:
                $ yzoom_var5 = zoom_var
            $ rotate_var5 = rotate_var
            $ xalign_var5 = xalign_var
            $ yalign_var5 = yalign_var
            $ image_found = False
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5

        if layer == 6 and not layer6_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer6_active = True
            if h_flip:
                $ xzoom_var6 = zoom_var * -1
            if not h_flip:
                $ xzoom_var6 = zoom_var
            if v_flip:
                $ yzoom_var6 = zoom_var * -1
            if not v_flip:
                $ yzoom_var6 = zoom_var
            $ rotate_var6 = rotate_var
            $ xalign_var6 = xalign_var
            $ yalign_var6 = yalign_var
            $ image_found = False
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6

        if layer == 7 and not layer7_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer7_active = True
            if h_flip:
                $ xzoom_var7 = zoom_var * -1
            if not h_flip:
                $ xzoom_var7 = zoom_var
            if v_flip:
                $ yzoom_var7 = zoom_var * -1
            if not v_flip:
                $ yzoom_var7 = zoom_var
            $ rotate_var7 = rotate_var
            $ xalign_var7 = xalign_var
            $ yalign_var7 = yalign_var
            $ image_found = False
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7

        if layer == 8 and not layer8_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer8_active = True
            if h_flip:
                $ xzoom_var8 = zoom_var * -1
            if not h_flip:
                $ xzoom_var8 = zoom_var
            if v_flip:
                $ yzoom_var8 = zoom_var * -1
            if not v_flip:
                $ yzoom_var8 = zoom_var
            $ rotate_var8 = rotate_var
            $ xalign_var8 = xalign_var
            $ yalign_var8 = yalign_var
            $ image_found = False
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8

        if layer == 9 and not layer9_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer9_active = True
            if h_flip:
                $ xzoom_var9 = zoom_var * -1
            if not h_flip:
                $ xzoom_var9 = zoom_var
            if v_flip:
                $ yzoom_var9 = zoom_var * -1
            if not v_flip:
                $ yzoom_var9 = zoom_var
            $ rotate_var9 = rotate_var
            $ xalign_var9 = xalign_var
            $ yalign_var9 = yalign_var
            $ image_found = False
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9

        if layer == 10 and not layer10_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer10_active = True
            if h_flip:
                $ xzoom_var10 = zoom_var * -1
            if not h_flip:
                $ xzoom_var10 = zoom_var
            if v_flip:
                $ yzoom_var10 = zoom_var * -1
            if not v_flip:
                $ yzoom_var10 = zoom_var
            $ rotate_var10 = rotate_var
            $ xalign_var10 = xalign_var
            $ yalign_var10 = yalign_var
            $ image_found = False
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10

        if layer == 11 and not layer11_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer11_active = True
            if h_flip:
                $ xzoom_var11 = zoom_var * -1
            if not h_flip:
                $ xzoom_var11 = zoom_var
            if v_flip:
                $ yzoom_var11 = zoom_var * -1
            if not v_flip:
                $ yzoom_var11 = zoom_var
            $ rotate_var11 = rotate_var
            $ xalign_var11 = xalign_var
            $ yalign_var11 = yalign_var
            $ image_found = False
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11

        if layer == 12 and not layer12_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer12_active = True
            if h_flip:
                $ xzoom_var12 = zoom_var * -1
            if not h_flip:
                $ xzoom_var12 = zoom_var
            if v_flip:
                $ yzoom_var12 = zoom_var * -1
            if not v_flip:
                $ yzoom_var12 = zoom_var
            $ rotate_var12 = rotate_var
            $ xalign_var12 = xalign_var
            $ yalign_var12 = yalign_var
            $ image_found = False
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12

        if layer == 13 and not layer13_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer13_active = True
            if h_flip:
                $ xzoom_var13 = zoom_var * -1
            if not h_flip:
                $ xzoom_var13 = zoom_var
            if v_flip:
                $ yzoom_var13 = zoom_var * -1
            if not v_flip:
                $ yzoom_var13 = zoom_var
            $ rotate_var13 = rotate_var
            $ xalign_var13 = xalign_var
            $ yalign_var13 = yalign_var
            $ image_found = False
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13

        if layer == 14 and not layer14_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer14_active = True
            if h_flip:
                $ xzoom_var14 = zoom_var * -1
            if not h_flip:
                $ xzoom_var14 = zoom_var
            if v_flip:
                $ yzoom_var14 = zoom_var * -1
            if not v_flip:
                $ yzoom_var14 = zoom_var
            $ rotate_var14 = rotate_var
            $ xalign_var14 = xalign_var
            $ yalign_var14 = yalign_var
            $ image_found = False
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14

        if layer == 15 and not layer15_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer15_active = True
            if h_flip:
                $ xzoom_var15 = zoom_var * -1
            if not h_flip:
                $ xzoom_var15 = zoom_var
            if v_flip:
                $ yzoom_var15 = zoom_var * -1
            if not v_flip:
                $ yzoom_var15 = zoom_var
            $ rotate_var15 = rotate_var
            $ xalign_var15 = xalign_var
            $ yalign_var15 = yalign_var
            $ image_found = False
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15

        if layer == 16 and not layer16_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer16_active = True
            if h_flip:
                $ xzoom_var16 = zoom_var * -1
            if not h_flip:
                $ xzoom_var16 = zoom_var
            if v_flip:
                $ yzoom_var16 = zoom_var * -1
            if not v_flip:
                $ yzoom_var16 = zoom_var
            $ rotate_var16 = rotate_var
            $ xalign_var16 = xalign_var
            $ yalign_var16 = yalign_var
            $ image_found = False
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16

        if layer == 17 and not layer17_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer17_active = True
            if h_flip:
                $ xzoom_var17 = zoom_var * -1
            if not h_flip:
                $ xzoom_var17 = zoom_var
            if v_flip:
                $ yzoom_var17 = zoom_var * -1
            if not v_flip:
                $ yzoom_var17 = zoom_var
            $ rotate_var17 = rotate_var
            $ xalign_var17 = xalign_var
            $ yalign_var17 = yalign_var
            $ image_found = False
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17

        if layer == 18 and not layer18_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer18_active = True
            if h_flip:
                $ xzoom_var18 = zoom_var * -1
            if not h_flip:
                $ xzoom_var18 = zoom_var
            if v_flip:
                $ yzoom_var18 = zoom_var * -1
            if not v_flip:
                $ yzoom_var18 = zoom_var
            $ rotate_var18 = rotate_var
            $ xalign_var18 = xalign_var
            $ yalign_var18 = yalign_var
            $ image_found = False
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18

        if layer == 19 and not layer19_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer19_active = True
            if h_flip:
                $ xzoom_var19 = zoom_var * -1
            if not h_flip:
                $ xzoom_var19 = zoom_var
            if v_flip:
                $ yzoom_var19 = zoom_var * -1
            if not v_flip:
                $ yzoom_var19 = zoom_var
            $ rotate_var19 = rotate_var
            $ xalign_var19 = xalign_var
            $ yalign_var19 = yalign_var
            $ image_found = False
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19

        if layer == 20 and not layer20_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer20_active = True
            if h_flip:
                $ xzoom_var20 = zoom_var * -1
            if not h_flip:
                $ xzoom_var20 = zoom_var
            if v_flip:
                $ yzoom_var20 = zoom_var * -1
            if not v_flip:
                $ yzoom_var20 = zoom_var
            $ rotate_var20 = rotate_var
            $ xalign_var20 = xalign_var
            $ yalign_var20 = yalign_var
            $ image_found = False
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20

        if layer == 21 and not layer21_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer21_active = True
            if h_flip:
                $ xzoom_var21 = zoom_var * -1
            if not h_flip:
                $ xzoom_var21 = zoom_var
            if v_flip:
                $ yzoom_var21 = zoom_var * -1
            if not v_flip:
                $ yzoom_var21 = zoom_var
            $ rotate_var21 = rotate_var
            $ xalign_var21 = xalign_var
            $ yalign_var21 = yalign_var
            $ image_found = False
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21

        if layer == 22 and not layer22_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer22_active = True
            if h_flip:
                $ xzoom_var22 = zoom_var * -1
            if not h_flip:
                $ xzoom_var22 = zoom_var
            if v_flip:
                $ yzoom_var22 = zoom_var * -1
            if not v_flip:
                $ yzoom_var22 = zoom_var
            $ rotate_var22 = rotate_var
            $ xalign_var22 = xalign_var
            $ yalign_var22 = yalign_var
            $ image_found = False
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22

        if layer == 23 and not layer23_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer23_active = True
            if h_flip:
                $ xzoom_var23 = zoom_var * -1
            if not h_flip:
                $ xzoom_var23 = zoom_var
            if v_flip:
                $ yzoom_var23 = zoom_var * -1
            if not v_flip:
                $ yzoom_var23 = zoom_var
            $ rotate_var23 = rotate_var
            $ xalign_var23 = xalign_var
            $ yalign_var23 = yalign_var
            $ image_found = False
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23

        if layer == 24 and not layer24_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer24_active = True
            if h_flip:
                $ xzoom_var24 = zoom_var * -1
            if not h_flip:
                $ xzoom_var24 = zoom_var
            if v_flip:
                $ yzoom_var24 = zoom_var * -1
            if not v_flip:
                $ yzoom_var24 = zoom_var
            $ rotate_var24 = rotate_var
            $ xalign_var24 = xalign_var
            $ yalign_var24 = yalign_var
            $ image_found = False
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24

        if layer == 25 and not layer25_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer25_active = True
            if h_flip:
                $ xzoom_var25 = zoom_var * -1
            if not h_flip:
                $ xzoom_var25 = zoom_var
            if v_flip:
                $ yzoom_var25 = zoom_var * -1
            if not v_flip:
                $ yzoom_var25 = zoom_var
            $ rotate_var25 = rotate_var
            $ xalign_var25 = xalign_var
            $ yalign_var25 = yalign_var
            $ image_found = False
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25

        if layer == 26 and not layer26_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer26_active = True
            if h_flip:
                $ xzoom_var26 = zoom_var * -1
            if not h_flip:
                $ xzoom_var26 = zoom_var
            if v_flip:
                $ yzoom_var26 = zoom_var * -1
            if not v_flip:
                $ yzoom_var26 = zoom_var
            $ rotate_var26 = rotate_var
            $ xalign_var26 = xalign_var
            $ yalign_var26 = yalign_var
            $ image_found = False
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26

        if layer == 27 and not layer27_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer27_active = True
            if h_flip:
                $ xzoom_var27 = zoom_var * -1
            if not h_flip:
                $ xzoom_var27 = zoom_var
            if v_flip:
                $ yzoom_var27 = zoom_var * -1
            if not v_flip:
                $ yzoom_var27 = zoom_var
            $ rotate_var27 = rotate_var
            $ xalign_var27 = xalign_var
            $ yalign_var27 = yalign_var
            $ image_found = False
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27

        if layer == 28 and not layer28_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer28_active = True
            if h_flip:
                $ xzoom_var28 = zoom_var * -1
            if not h_flip:
                $ xzoom_var28 = zoom_var
            if v_flip:
                $ yzoom_var28 = zoom_var * -1
            if not v_flip:
                $ yzoom_var28 = zoom_var
            $ rotate_var28 = rotate_var
            $ xalign_var28 = xalign_var
            $ yalign_var28 = yalign_var
            $ image_found = False
            show expression("[layers[27]]"):
                rotate rotate_var28 xzoom xzoom_var28 yzoom yzoom_var28 xalign xalign_var28 yalign yalign_var28

        if layer == 29 and not layer29_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer29_active = True
            if h_flip:
                $ xzoom_var29 = zoom_var * -1
            if not h_flip:
                $ xzoom_var29 = zoom_var
            if v_flip:
                $ yzoom_var29 = zoom_var * -1
            if not v_flip:
                $ yzoom_var29 = zoom_var
            $ rotate_var29 = rotate_var
            $ xalign_var29 = xalign_var
            $ yalign_var29 = yalign_var
            $ image_found = False
            show expression("[layers[28]]"):
                rotate rotate_var29 xzoom xzoom_var29 yzoom yzoom_var29 xalign xalign_var29 yalign yalign_var29

        if layer == 30 and not layer30_active:
            $ layers.append(file_location)
            $ zoom_var = 1.0
            $ xzoom_var = 0.0
            $ yzoom_var = 0.0
            $ xalign_var = 0.50
            $ yalign_var = 0.50
            $ rotate_var = 0
            $ layer30_active = True
            if h_flip:
                $ xzoom_var30 = zoom_var * -1
            if not h_flip:
                $ xzoom_var30 = zoom_var
            if v_flip:
                $ yzoom_var30 = zoom_var * -1
            if not v_flip:
                $ yzoom_var30 = zoom_var
            $ rotate_var30 = rotate_var
            $ xalign_var30 = xalign_var
            $ yalign_var30 = yalign_var
            $ image_found = False
            show expression("[layers[29]]"):
                rotate rotate_var30 xzoom xzoom_var30 yzoom yzoom_var30 xalign xalign_var30 yalign yalign_var30

    jump image_loop


label restart_image:
    if move_layers_simultan:
        if layer == 1:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1

        if layer == 2:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2

        if layer == 3:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3

        if layer == 4:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4

        if layer == 5:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5

        if layer == 6:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6

        if layer == 7:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7

        if layer == 8:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8

        if layer == 9:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9

        if layer == 10:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10

        if layer == 11:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11

        if layer == 12:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12

        if layer == 13:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13

        if layer == 14:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14

        if layer == 15:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15

        if layer == 16:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16

        if layer == 17:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17

        if layer == 18:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18

        if layer == 19:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19

        if layer == 20:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20

        if layer == 21:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21

        if layer == 22:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22

        if layer == 23:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23

        if layer == 24:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24

        if layer == 25:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25

        if layer == 26:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            $ rotate_var26 = round(rotate_var25 - diff_rotate_var26, 2)
            $ xalign_var26 = round(xalign_var25 - diff_xalign_var26, 2)
            $ yalign_var26 = round(yalign_var25 - diff_yalign_var26, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26

        if layer == 27:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            $ rotate_var26 = round(rotate_var25 - diff_rotate_var26, 2)
            $ xalign_var26 = round(xalign_var25 - diff_xalign_var26, 2)
            $ yalign_var26 = round(yalign_var25 - diff_yalign_var26, 2)
            $ rotate_var27 = round(rotate_var26 - diff_rotate_var27, 2)
            $ xalign_var27 = round(xalign_var26 - diff_xalign_var27, 2)
            $ yalign_var27 = round(yalign_var26 - diff_yalign_var27, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27

        if layer == 28:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            $ rotate_var26 = round(rotate_var25 - diff_rotate_var26, 2)
            $ xalign_var26 = round(xalign_var25 - diff_xalign_var26, 2)
            $ yalign_var26 = round(yalign_var25 - diff_yalign_var26, 2)
            $ rotate_var27 = round(rotate_var26 - diff_rotate_var27, 2)
            $ xalign_var27 = round(xalign_var26 - diff_xalign_var27, 2)
            $ yalign_var27 = round(yalign_var26 - diff_yalign_var27, 2)
            $ rotate_var28 = round(rotate_var27 - diff_rotate_var28, 2)
            $ xalign_var28 = round(xalign_var27 - diff_xalign_var28, 2)
            $ yalign_var28 = round(yalign_var27 - diff_yalign_var28, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27
            show expression("[layers[27]]"):
                rotate rotate_var28 xzoom xzoom_var28 yzoom yzoom_var28 xalign xalign_var28 yalign yalign_var28

        if layer == 29:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            $ rotate_var26 = round(rotate_var25 - diff_rotate_var26, 2)
            $ xalign_var26 = round(xalign_var25 - diff_xalign_var26, 2)
            $ yalign_var26 = round(yalign_var25 - diff_yalign_var26, 2)
            $ rotate_var27 = round(rotate_var26 - diff_rotate_var27, 2)
            $ xalign_var27 = round(xalign_var26 - diff_xalign_var27, 2)
            $ yalign_var27 = round(yalign_var26 - diff_yalign_var27, 2)
            $ rotate_var28 = round(rotate_var27 - diff_rotate_var28, 2)
            $ xalign_var28 = round(xalign_var27 - diff_xalign_var28, 2)
            $ yalign_var28 = round(yalign_var27 - diff_yalign_var28, 2)
            $ rotate_var29 = round(rotate_var28 - diff_rotate_var29, 2)
            $ xalign_var29 = round(xalign_var28 - diff_xalign_var29, 2)
            $ yalign_var29 = round(yalign_var28 - diff_yalign_var29, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27
            show expression("[layers[27]]"):
                rotate rotate_var28 xzoom xzoom_var28 yzoom yzoom_var28 xalign xalign_var28 yalign yalign_var28
            show expression("[layers[28]]"):
                rotate rotate_var29 xzoom xzoom_var29 yzoom yzoom_var29 xalign xalign_var29 yalign yalign_var29

        if layer == 30:
            $ rotate_var1 = round(rotate_var, 2)
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            $ rotate_var2 = round(rotate_var1 - diff_rotate_var2, 2)
            $ xalign_var2 = round(xalign_var1 - diff_xalign_var2, 2)
            $ yalign_var2 = round(yalign_var1 - diff_yalign_var2, 2)
            $ rotate_var3 = round(rotate_var2 - diff_rotate_var3, 2)
            $ xalign_var3 = round(xalign_var2 - diff_xalign_var3, 2)
            $ yalign_var3 = round(yalign_var2 - diff_yalign_var3, 2)
            $ rotate_var4 = round(rotate_var3 - diff_rotate_var4, 2)
            $ xalign_var4 = round(xalign_var3 - diff_xalign_var4, 2)
            $ yalign_var4 = round(yalign_var3 - diff_yalign_var4, 2)
            $ rotate_var5 = round(rotate_var4 - diff_rotate_var5, 2)
            $ xalign_var5 = round(xalign_var4 - diff_xalign_var5, 2)
            $ yalign_var5 = round(yalign_var4 - diff_yalign_var5, 2)
            $ rotate_var6 = round(rotate_var5 - diff_rotate_var6, 2)
            $ xalign_var6 = round(xalign_var5 - diff_xalign_var6, 2)
            $ yalign_var6 = round(yalign_var5 - diff_yalign_var6, 2)
            $ rotate_var7 = round(rotate_var6 - diff_rotate_var7, 2)
            $ xalign_var7 = round(xalign_var6 - diff_xalign_var7, 2)
            $ yalign_var7 = round(yalign_var6 - diff_yalign_var7, 2)
            $ rotate_var8 = round(rotate_var7 - diff_rotate_var8, 2)
            $ xalign_var8 = round(xalign_var7 - diff_xalign_var8, 2)
            $ yalign_var8 = round(yalign_var7 - diff_yalign_var8, 2)
            $ rotate_var9 = round(rotate_var8 - diff_rotate_var9, 2)
            $ xalign_var9 = round(xalign_var8 - diff_xalign_var9, 2)
            $ yalign_var9 = round(yalign_var8 - diff_yalign_var9, 2)
            $ rotate_var10 = round(rotate_var9 - diff_rotate_var10, 2)
            $ xalign_var10 = round(xalign_var9 - diff_xalign_var10, 2)
            $ yalign_var10 = round(yalign_var9 - diff_yalign_var10, 2)
            $ rotate_var11 = round(rotate_var10 - diff_rotate_var11, 2)
            $ xalign_var11 = round(xalign_var10 - diff_xalign_var11, 2)
            $ yalign_var11 = round(yalign_var10 - diff_yalign_var11, 2)
            $ rotate_var12 = round(rotate_var11 - diff_rotate_var12, 2)
            $ xalign_var12 = round(xalign_var11 - diff_xalign_var12, 2)
            $ yalign_var12 = round(yalign_var11 - diff_yalign_var12, 2)
            $ rotate_var13 = round(rotate_var12 - diff_rotate_var13, 2)
            $ xalign_var13 = round(xalign_var12 - diff_xalign_var13, 2)
            $ yalign_var13 = round(yalign_var12 - diff_yalign_var13, 2)
            $ rotate_var14 = round(rotate_var13 - diff_rotate_var14, 2)
            $ xalign_var14 = round(xalign_var13 - diff_xalign_var14, 2)
            $ yalign_var14 = round(yalign_var13 - diff_yalign_var14, 2)
            $ rotate_var15 = round(rotate_var14 - diff_rotate_var15, 2)
            $ xalign_var15 = round(xalign_var14 - diff_xalign_var15, 2)
            $ yalign_var15 = round(yalign_var14 - diff_yalign_var15, 2)
            $ rotate_var16 = round(rotate_var15 - diff_rotate_var16, 2)
            $ xalign_var16 = round(xalign_var15 - diff_xalign_var16, 2)
            $ yalign_var16 = round(yalign_var15 - diff_yalign_var16, 2)
            $ rotate_var17 = round(rotate_var16 - diff_rotate_var17, 2)
            $ xalign_var17 = round(xalign_var16 - diff_xalign_var17, 2)
            $ yalign_var17 = round(yalign_var16 - diff_yalign_var17, 2)
            $ rotate_var18 = round(rotate_var17 - diff_rotate_var18, 2)
            $ xalign_var18 = round(xalign_var17 - diff_xalign_var18, 2)
            $ yalign_var18 = round(yalign_var17 - diff_yalign_var18, 2)
            $ rotate_var19 = round(rotate_var18 - diff_rotate_var19, 2)
            $ xalign_var19 = round(xalign_var18 - diff_xalign_var19, 2)
            $ yalign_var19 = round(yalign_var18 - diff_yalign_var19, 2)
            $ rotate_var20 = round(rotate_var19 - diff_rotate_var20, 2)
            $ xalign_var20 = round(xalign_var19 - diff_xalign_var20, 2)
            $ yalign_var20 = round(yalign_var19 - diff_yalign_var20, 2)
            $ rotate_var21 = round(rotate_var20 - diff_rotate_var21, 2)
            $ xalign_var21 = round(xalign_var20 - diff_xalign_var21, 2)
            $ yalign_var21 = round(yalign_var20 - diff_yalign_var21, 2)
            $ rotate_var22 = round(rotate_var21 - diff_rotate_var22, 2)
            $ xalign_var22 = round(xalign_var21 - diff_xalign_var22, 2)
            $ yalign_var22 = round(yalign_var21 - diff_yalign_var22, 2)
            $ rotate_var23 = round(rotate_var22 - diff_rotate_var23, 2)
            $ xalign_var23 = round(xalign_var22 - diff_xalign_var23, 2)
            $ yalign_var23 = round(yalign_var22 - diff_yalign_var23, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var24 = round(rotate_var23 - diff_rotate_var24, 2)
            $ xalign_var24 = round(xalign_var23 - diff_xalign_var24, 2)
            $ yalign_var24 = round(yalign_var23 - diff_yalign_var24, 2)
            $ rotate_var25 = round(rotate_var24 - diff_rotate_var25, 2)
            $ xalign_var25 = round(xalign_var24 - diff_xalign_var25, 2)
            $ yalign_var25 = round(yalign_var24 - diff_yalign_var25, 2)
            $ rotate_var26 = round(rotate_var25 - diff_rotate_var26, 2)
            $ xalign_var26 = round(xalign_var25 - diff_xalign_var26, 2)
            $ yalign_var26 = round(yalign_var25 - diff_yalign_var26, 2)
            $ rotate_var27 = round(rotate_var26 - diff_rotate_var27, 2)
            $ xalign_var27 = round(xalign_var26 - diff_xalign_var27, 2)
            $ yalign_var27 = round(yalign_var26 - diff_yalign_var27, 2)
            $ rotate_var28 = round(rotate_var27 - diff_rotate_var28, 2)
            $ xalign_var28 = round(xalign_var27 - diff_xalign_var28, 2)
            $ yalign_var28 = round(yalign_var27 - diff_yalign_var28, 2)
            $ rotate_var29 = round(rotate_var28 - diff_rotate_var29, 2)
            $ xalign_var29 = round(xalign_var28 - diff_xalign_var29, 2)
            $ yalign_var29 = round(yalign_var28 - diff_yalign_var29, 2)
            $ rotate_var30 = round(rotate_var29 - diff_rotate_var30, 2)
            $ xalign_var30 = round(xalign_var29 - diff_xalign_var30, 2)
            $ yalign_var30 = round(yalign_var29 - diff_yalign_var30, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27
            show expression("[layers[27]]"):
                rotate rotate_var28 xzoom xzoom_var28 yzoom yzoom_var28 xalign xalign_var28 yalign yalign_var28
            show expression("[layers[28]]"):
                rotate rotate_var29 xzoom xzoom_var29 yzoom yzoom_var29 xalign xalign_var29 yalign yalign_var29
            show expression("[layers[29]]"):
                rotate rotate_var30 xzoom xzoom_var30 yzoom yzoom_var30 xalign xalign_var30 yalign yalign_var30

        jump image_loop

    if not move_layers_simultan:
        if selected_layer == 1:
            if h_flip:
                $ xzoom_var1 = round(zoom_var, 2) * -1
                $ h_flip_var1 = True
            if not h_flip:
                $ xzoom_var1 = round(zoom_var, 2)
                $ h_flip_var1 = False
            if v_flip:
                $ yzoom_var1 = round(zoom_var, 2) * -1
                $ v_flip_var1 = True
            if not v_flip:
                $ yzoom_var1 = round(zoom_var, 2)
                $ v_flip_var1 = False
            $ rotate_var1 = rotate_var
            $ xalign_var1 = round(xalign_var, 2)
            $ yalign_var1 = round(yalign_var, 2)
            show expression("[layers[0]]"):
                rotate rotate_var1 xzoom xzoom_var1 yzoom yzoom_var1 xalign xalign_var1 yalign yalign_var1

        if selected_layer == 2:
            if h_flip:
                $ xzoom_var2 = round(zoom_var, 2) * -1
                $ h_flip_var2 = True
            if not h_flip:
                $ xzoom_var2 = round(zoom_var, 2)
                $ h_flip_var2 = False
            if v_flip:
                $ yzoom_var2 = round(zoom_var, 2) * -1
                $ v_flip_var2 = True
            if not v_flip:
                $ yzoom_var2 = round(zoom_var, 2)
                $ v_flip_var2 = False
            $ rotate_var2 = rotate_var
            $ xalign_var2 = round(xalign_var, 2)
            $ yalign_var2 = round(yalign_var, 2)
            show expression("[layers[1]]"):
                rotate rotate_var2 xzoom xzoom_var2 yzoom yzoom_var2 xalign xalign_var2 yalign yalign_var2

        if selected_layer == 3:
            if h_flip:
                $ xzoom_var3 = round(zoom_var, 2) * -1
                $ h_flip_var3 = True
            if not h_flip:
                $ xzoom_var3 = round(zoom_var, 2)
                $ h_flip_var3 = False
            if v_flip:
                $ yzoom_var3 = round(zoom_var, 2) * -1
                $ v_flip_var3 = True
            if not v_flip:
                $ yzoom_var3 = round(zoom_var, 2)
                $ v_flip_var3 = False
            $ rotate_var3 = rotate_var
            $ xalign_var3 = round(xalign_var, 2)
            $ yalign_var3 = round(yalign_var, 2)
            show expression("[layers[2]]"):
                rotate rotate_var3 xzoom xzoom_var3 yzoom yzoom_var3 xalign xalign_var3 yalign yalign_var3

        if selected_layer == 4:
            if h_flip:
                $ xzoom_var4 = round(zoom_var, 2) * -1
                $ h_flip_var4 = True
            if not h_flip:
                $ xzoom_var4 = round(zoom_var, 2)
                $ h_flip_var4 = False
            if v_flip:
                $ yzoom_var4 = round(zoom_var, 2) * -1
                $ v_flip_var4 = True
            if not v_flip:
                $ yzoom_var4 = round(zoom_var, 2)
                $ v_flip_var4 = False
            $ rotate_var4 = rotate_var
            $ xalign_var4 = round(xalign_var, 2)
            $ yalign_var4 = round(yalign_var, 2)
            show expression("[layers[3]]"):
                rotate rotate_var4 xzoom xzoom_var4 yzoom yzoom_var4 xalign xalign_var4 yalign yalign_var4

        if selected_layer == 5:
            if h_flip:
                $ xzoom_var5 = round(zoom_var, 2) * -1
                $ h_flip_var5 = True
            if not h_flip:
                $ xzoom_var5 = round(zoom_var, 2)
                $ h_flip_var5 = False
            if v_flip:
                $ yzoom_var5 = round(zoom_var, 2) * -1
                $ v_flip_var5 = True
            if not v_flip:
                $ yzoom_var5 = round(zoom_var, 2)
                $ v_flip_var5 = False
            $ rotate_var5 = rotate_var
            $ xalign_var5 = round(xalign_var, 2)
            $ yalign_var5 = round(yalign_var, 2)
            show expression("[layers[4]]"):
                rotate rotate_var5 xzoom xzoom_var5 yzoom yzoom_var5 xalign xalign_var5 yalign yalign_var5

        if selected_layer == 6:
            if h_flip:
                $ xzoom_var6 = round(zoom_var, 2) * -1
                $ h_flip_var6 = True
            if not h_flip:
                $ xzoom_var6 = round(zoom_var, 2)
                $ h_flip_var6 = False
            if v_flip:
                $ yzoom_var6 = round(zoom_var, 2) * -1
                $ v_flip_var6 = True
            if not v_flip:
                $ yzoom_var6 = round(zoom_var, 2)
                $ v_flip_var6 = False
            $ rotate_var6 = rotate_var
            $ xalign_var6 = round(xalign_var, 2)
            $ yalign_var6 = round(yalign_var, 2)
            show expression("[layers[5]]"):
                rotate rotate_var6 xzoom xzoom_var6 yzoom yzoom_var6 xalign xalign_var6 yalign yalign_var6

        if selected_layer == 7:
            if h_flip:
                $ xzoom_var7 = round(zoom_var, 2) * -1
                $ h_flip_var7 = True
            if not h_flip:
                $ xzoom_var7 = round(zoom_var, 2)
                $ h_flip_var7 = False
            if v_flip:
                $ yzoom_var7 = round(zoom_var, 2) * -1
                $ v_flip_var7 = True
            if not v_flip:
                $ yzoom_var7 = round(zoom_var, 2)
                $ v_flip_var7 = False
            $ rotate_var7 = rotate_var
            $ xalign_var7 = round(xalign_var, 2)
            $ yalign_var7 = round(yalign_var, 2)
            show expression("[layers[6]]"):
                rotate rotate_var7 xzoom xzoom_var7 yzoom yzoom_var7 xalign xalign_var7 yalign yalign_var7

        if selected_layer == 8:
            if h_flip:
                $ xzoom_var8 = round(zoom_var, 2) * -1
                $ h_flip_var8 = True
            if not h_flip:
                $ xzoom_var8 = round(zoom_var, 2)
                $ h_flip_var8 = False
            if v_flip:
                $ yzoom_var8 = round(zoom_var, 2) * -1
                $ v_flip_var8 = True
            if not v_flip:
                $ yzoom_var8 = round(zoom_var, 2)
                $ v_flip_var8 = False
            $ rotate_var8 = rotate_var
            $ xalign_var8 = round(xalign_var, 2)
            $ yalign_var8 = round(yalign_var, 2)
            show expression("[layers[7]]"):
                rotate rotate_var8 xzoom xzoom_var8 yzoom yzoom_var8 xalign xalign_var8 yalign yalign_var8

        if selected_layer == 9:
            if h_flip:
                $ xzoom_var9 = round(zoom_var, 2) * -1
                $ h_flip_var9 = True
            if not h_flip:
                $ xzoom_var9 = round(zoom_var, 2)
                $ h_flip_var9 = False
            if v_flip:
                $ yzoom_var9 = round(zoom_var, 2) * -1
                $ v_flip_var9 = True
            if not v_flip:
                $ yzoom_var9 = round(zoom_var, 2)
                $ v_flip_var9 = False
            $ rotate_var9 = rotate_var
            $ xalign_var9 = round(xalign_var, 2)
            $ yalign_var9 = round(yalign_var, 2)
            show expression("[layers[8]]"):
                rotate rotate_var9 xzoom xzoom_var9 yzoom yzoom_var9 xalign xalign_var9 yalign yalign_var9

        if selected_layer == 10:
            if h_flip:
                $ xzoom_var10 = round(zoom_var, 2) * -1
                $ h_flip_var10 = True
            if not h_flip:
                $ xzoom_var10 = round(zoom_var, 2)
                $ h_flip_var10 = False
            if v_flip:
                $ yzoom_var10 = round(zoom_var, 2) * -1
                $ v_flip_var10 = True
            if not v_flip:
                $ yzoom_var10 = round(zoom_var, 2)
                $ v_flip_var10 = False
            $ rotate_var10 = rotate_var
            $ xalign_var10 = round(xalign_var, 2)
            $ yalign_var10 = round(yalign_var, 2)
            show expression("[layers[9]]"):
                rotate rotate_var10 xzoom xzoom_var10 yzoom yzoom_var10 xalign xalign_var10 yalign yalign_var10

        if selected_layer == 11:
            if h_flip:
                $ xzoom_var11 = round(zoom_var, 2) * -1
                $ h_flip_var11 = True
            if not h_flip:
                $ xzoom_var11 = round(zoom_var, 2)
                $ h_flip_var11 = False
            if v_flip:
                $ yzoom_var11 = round(zoom_var, 2) * -1
                $ v_flip_var11 = True
            if not v_flip:
                $ yzoom_var11 = round(zoom_var, 2)
                $ v_flip_var11 = False
            $ rotate_var11 = rotate_var
            $ xalign_var11 = round(xalign_var, 2)
            $ yalign_var11 = round(yalign_var, 2)
            show expression("[layers[10]]"):
                rotate rotate_var11 xzoom xzoom_var11 yzoom yzoom_var11 xalign xalign_var11 yalign yalign_var11

        if selected_layer == 12:
            if h_flip:
                $ xzoom_var12 = round(zoom_var, 2) * -1
                $ h_flip_var12 = True
            if not h_flip:
                $ xzoom_var12 = round(zoom_var, 2)
                $ h_flip_var12 = False
            if v_flip:
                $ yzoom_var12 = round(zoom_var, 2) * -1
                $ v_flip_var12 = True
            if not v_flip:
                $ yzoom_var12 = round(zoom_var, 2)
                $ v_flip_var12 = False
            $ rotate_var12 = rotate_var
            $ xalign_var12 = round(xalign_var, 2)
            $ yalign_var12 = round(yalign_var, 2)
            show expression("[layers[11]]"):
                rotate rotate_var12 xzoom xzoom_var12 yzoom yzoom_var12 xalign xalign_var12 yalign yalign_var12

        if selected_layer == 13:
            if h_flip:
                $ xzoom_var13 = round(zoom_var, 2) * -1
                $ h_flip_var13 = True
            if not h_flip:
                $ xzoom_var13 = round(zoom_var, 2)
                $ h_flip_var13 = False
            if v_flip:
                $ yzoom_var13 = round(zoom_var, 2) * -1
                $ v_flip_var13 = True
            if not v_flip:
                $ yzoom_var13 = round(zoom_var, 2)
                $ v_flip_var13 = False
            $ rotate_var13 = rotate_var
            $ xalign_var13 = round(xalign_var, 2)
            $ yalign_var13 = round(yalign_var, 2)
            show expression("[layers[12]]"):
                rotate rotate_var13 xzoom xzoom_var13 yzoom yzoom_var13 xalign xalign_var13 yalign yalign_var13

        if selected_layer == 14:
            if h_flip:
                $ xzoom_var14 = round(zoom_var, 2) * -1
                $ h_flip_var14 = True
            if not h_flip:
                $ xzoom_var14 = round(zoom_var, 2)
                $ h_flip_var14 = False
            if v_flip:
                $ yzoom_var14 = round(zoom_var, 2) * -1
                $ v_flip_var14 = True
            if not v_flip:
                $ yzoom_var14 = round(zoom_var, 2)
                $ v_flip_var14 = False
            $ rotate_var14 = rotate_var
            $ xalign_var14 = round(xalign_var, 2)
            $ yalign_var14 = round(yalign_var, 2)
            show expression("[layers[13]]"):
                rotate rotate_var14 xzoom xzoom_var14 yzoom yzoom_var14 xalign xalign_var14 yalign yalign_var14

        if selected_layer == 15:
            if h_flip:
                $ xzoom_var15 = round(zoom_var, 2) * -1
                $ h_flip_var15 = True
            if not h_flip:
                $ xzoom_var15 = round(zoom_var, 2)
                $ h_flip_var15 = False
            if v_flip:
                $ yzoom_var15 = round(zoom_var, 2) * -1
                $ v_flip_var15 = True
            if not v_flip:
                $ yzoom_var15 = round(zoom_var, 2)
                $ v_flip_var15 = False
            $ rotate_var15 = rotate_var
            $ xalign_var15 = round(xalign_var, 2)
            $ yalign_var15 = round(yalign_var, 2)
            show expression("[layers[14]]"):
                rotate rotate_var15 xzoom xzoom_var15 yzoom yzoom_var15 xalign xalign_var15 yalign yalign_var15

        if selected_layer == 16:
            if h_flip:
                $ xzoom_var16 = round(zoom_var, 2) * -1
                $ h_flip_var16 = True
            if not h_flip:
                $ xzoom_var16 = round(zoom_var, 2)
                $ h_flip_var16 = False
            if v_flip:
                $ yzoom_var16 = round(zoom_var, 2) * -1
                $ v_flip_var16 = True
            if not v_flip:
                $ yzoom_var16 = round(zoom_var, 2)
                $ v_flip_var16 = False
            $ rotate_var16 = rotate_var
            $ xalign_var16 = round(xalign_var, 2)
            $ yalign_var16 = round(yalign_var, 2)
            show expression("[layers[15]]"):
                rotate rotate_var16 xzoom xzoom_var16 yzoom yzoom_var16 xalign xalign_var16 yalign yalign_var16

        if selected_layer == 17:
            if h_flip:
                $ xzoom_var17 = round(zoom_var, 2) * -1
                $ h_flip_var17 = True
            if not h_flip:
                $ xzoom_var17 = round(zoom_var, 2)
                $ h_flip_var17 = False
            if v_flip:
                $ yzoom_var17 = round(zoom_var, 2) * -1
                $ v_flip_var17 = True
            if not v_flip:
                $ yzoom_var17 = round(zoom_var, 2)
                $ v_flip_var17 = False
            $ rotate_var17 = rotate_var
            $ xalign_var17 = round(xalign_var, 2)
            $ yalign_var17 = round(yalign_var, 2)
            show expression("[layers[16]]"):
                rotate rotate_var17 xzoom xzoom_var17 yzoom yzoom_var17 xalign xalign_var17 yalign yalign_var17

        if selected_layer == 18:
            if h_flip:
                $ xzoom_var18 = round(zoom_var, 2) * -1
                $ h_flip_var18 = True
            if not h_flip:
                $ xzoom_var18 = round(zoom_var, 2)
                $ h_flip_var18 = False
            if v_flip:
                $ yzoom_var18 = round(zoom_var, 2) * -1
                $ v_flip_var18 = True
            if not v_flip:
                $ yzoom_var18 = round(zoom_var, 2)
                $ v_flip_var18 = False
            $ rotate_var18 = rotate_var
            $ xalign_var18 = round(xalign_var, 2)
            $ yalign_var18 = round(yalign_var, 2)
            show expression("[layers[17]]"):
                rotate rotate_var18 xzoom xzoom_var18 yzoom yzoom_var18 xalign xalign_var18 yalign yalign_var18

        if selected_layer == 19:
            if h_flip:
                $ xzoom_var19 = round(zoom_var, 2) * -1
                $ h_flip_var19 = True
            if not h_flip:
                $ xzoom_var19 = round(zoom_var, 2)
                $ h_flip_var19 = False
            if v_flip:
                $ yzoom_var19 = round(zoom_var, 2) * -1
                $ v_flip_var19 = True
            if not v_flip:
                $ yzoom_var19 = round(zoom_var, 2)
                $ v_flip_var19 = False
            $ rotate_var19 = rotate_var
            $ xalign_var19 = round(xalign_var, 2)
            $ yalign_var19 = round(yalign_var, 2)
            show expression("[layers[18]]"):
                rotate rotate_var19 xzoom xzoom_var19 yzoom yzoom_var19 xalign xalign_var19 yalign yalign_var19

        if selected_layer == 20:
            if h_flip:
                $ xzoom_var20 = round(zoom_var, 2) * -1
                $ h_flip_var20 = True
            if not h_flip:
                $ xzoom_var20 = round(zoom_var, 2)
                $ h_flip_var20 = False
            if v_flip:
                $ yzoom_var20 = round(zoom_var, 2) * -1
                $ v_flip_var20 = True
            if not v_flip:
                $ yzoom_var20 = round(zoom_var, 2)
                $ v_flip_var20 = False
            $ rotate_var20 = rotate_var
            $ xalign_var20 = round(xalign_var, 2)
            $ yalign_var20 = round(yalign_var, 2)
            show expression("[layers[19]]"):
                rotate rotate_var20 xzoom xzoom_var20 yzoom yzoom_var20 xalign xalign_var20 yalign yalign_var20

        if selected_layer == 21:
            if h_flip:
                $ xzoom_var21 = round(zoom_var, 2) * -1
                $ h_flip_var21 = True
            if not h_flip:
                $ xzoom_var21 = round(zoom_var, 2)
                $ h_flip_var21 = False
            if v_flip:
                $ yzoom_var21 = round(zoom_var, 2) * -1
                $ v_flip_var21 = True
            if not v_flip:
                $ yzoom_var21 = round(zoom_var, 2)
                $ v_flip_var21 = False
            $ rotate_var21 = rotate_var
            $ xalign_var21 = round(xalign_var, 2)
            $ yalign_var21 = round(yalign_var, 2)
            show expression("[layers[20]]"):
                rotate rotate_var21 xzoom xzoom_var21 yzoom yzoom_var21 xalign xalign_var21 yalign yalign_var21

        if selected_layer == 22:
            if h_flip:
                $ xzoom_var22 = round(zoom_var, 2) * -1
                $ h_flip_var22 = True
            if not h_flip:
                $ xzoom_var22 = round(zoom_var, 2)
                $ h_flip_var22 = False
            if v_flip:
                $ yzoom_var22 = round(zoom_var, 2) * -1
                $ v_flip_var22 = True
            if not v_flip:
                $ yzoom_var22 = round(zoom_var, 2)
                $ v_flip_var22 = False
            $ rotate_var22 = rotate_var
            $ xalign_var22 = round(xalign_var, 2)
            $ yalign_var22 = round(yalign_var, 2)
            show expression("[layers[21]]"):
                rotate rotate_var22 xzoom xzoom_var22 yzoom yzoom_var22 xalign xalign_var22 yalign yalign_var22

        if selected_layer == 23:
            if h_flip:
                $ xzoom_var23 = round(zoom_var, 2) * -1
                $ h_flip_var23 = True
            if not h_flip:
                $ xzoom_var23 = round(zoom_var, 2)
                $ h_flip_var23 = False
            if v_flip:
                $ yzoom_var23 = round(zoom_var, 2) * -1
                $ v_flip_var23 = True
            if not v_flip:
                $ yzoom_var23 = round(zoom_var, 2)
                $ v_flip_var23 = False
            $ rotate_var23 = rotate_var
            $ xalign_var23 = round(xalign_var, 2)
            $ yalign_var23 = round(yalign_var, 2)
            show expression("[layers[22]]"):
                rotate rotate_var23 xzoom xzoom_var23 yzoom yzoom_var23 xalign xalign_var23 yalign yalign_var23

        if selected_layer == 24:
            if h_flip:
                $ xzoom_var24 = round(zoom_var, 2) * -1
                $ h_flip_var24 = True
            if not h_flip:
                $ xzoom_var24 = round(zoom_var, 2)
                $ h_flip_var24 = False
            if v_flip:
                $ yzoom_var24 = round(zoom_var, 2) * -1
                $ v_flip_var24 = True
            if not v_flip:
                $ yzoom_var24 = round(zoom_var, 2)
                $ v_flip_var24 = False
            $ rotate_var24 = rotate_var
            $ xalign_var24 = round(xalign_var, 2)
            $ yalign_var24 = round(yalign_var, 2)
            show expression("[layers[23]]"):
                rotate rotate_var24 xzoom xzoom_var24 yzoom yzoom_var24 xalign xalign_var24 yalign yalign_var24

        if selected_layer == 25:
            if h_flip:
                $ xzoom_var25 = round(zoom_var, 2) * -1
                $ h_flip_var25 = True
            if not h_flip:
                $ xzoom_var25 = round(zoom_var, 2)
                $ h_flip_var25 = False
            if v_flip:
                $ yzoom_var25 = round(zoom_var, 2) * -1
                $ v_flip_var25 = True
            if not v_flip:
                $ yzoom_var25 = round(zoom_var, 2)
                $ v_flip_var25 = False
            $ rotate_var25 = rotate_var
            $ xalign_var25 = round(xalign_var, 2)
            $ yalign_var25 = round(yalign_var, 2)
            show expression("[layers[24]]"):
                rotate rotate_var25 xzoom xzoom_var25 yzoom yzoom_var25 xalign xalign_var25 yalign yalign_var25

        if selected_layer == 26:
            if h_flip:
                $ xzoom_var26 = round(zoom_var, 2) * -1
                $ h_flip_var26 = True
            if not h_flip:
                $ xzoom_var26 = round(zoom_var, 2)
                $ h_flip_var26 = False
            if v_flip:
                $ yzoom_var26 = round(zoom_var, 2) * -1
                $ v_flip_var26 = True
            if not v_flip:
                $ yzoom_var26 = round(zoom_var, 2)
                $ v_flip_var26 = False
            $ rotate_var26 = rotate_var
            $ xalign_var26 = round(xalign_var, 2)
            $ yalign_var26 = round(yalign_var, 2)
            show expression("[layers[25]]"):
                rotate rotate_var26 xzoom xzoom_var26 yzoom yzoom_var26 xalign xalign_var26 yalign yalign_var26

        if selected_layer == 27:
            if h_flip:
                $ xzoom_var27 = round(zoom_var, 2) * -1
                $ h_flip_var27 = True
            if not h_flip:
                $ xzoom_var27 = round(zoom_var, 2)
                $ h_flip_var27 = False
            if v_flip:
                $ yzoom_var27 = round(zoom_var, 2) * -1
                $ v_flip_var27 = True
            if not v_flip:
                $ yzoom_var27 = round(zoom_var, 2)
                $ v_flip_var27 = False
            $ rotate_var27 = rotate_var
            $ xalign_var27 = round(xalign_var, 2)
            $ yalign_var27 = round(yalign_var, 2)
            show expression("[layers[26]]"):
                rotate rotate_var27 xzoom xzoom_var27 yzoom yzoom_var27 xalign xalign_var27 yalign yalign_var27

        if selected_layer == 28:
            if h_flip:
                $ xzoom_var28 = round(zoom_var, 2) * -1
                $ h_flip_var28 = True
            if not h_flip:
                $ xzoom_var28 = round(zoom_var, 2)
                $ h_flip_var28 = False
            if v_flip:
                $ yzoom_var28 = round(zoom_var, 2) * -1
                $ v_flip_var28 = True
            if not v_flip:
                $ yzoom_var28 = round(zoom_var, 2)
                $ v_flip_var28 = False
            $ rotate_var28 = rotate_var
            $ xalign_var28 = round(xalign_var, 2)
            $ yalign_var28 = round(yalign_var, 2)
            show expression("[layers[27]]"):
                rotate rotate_var28 xzoom xzoom_var28 yzoom yzoom_var28 xalign xalign_var28 yalign yalign_var28

        if selected_layer == 29:
            if h_flip:
                $ xzoom_var29 = round(zoom_var, 2) * -1
                $ h_flip_var29 = True
            if not h_flip:
                $ xzoom_var29 = round(zoom_var, 2)
                $ h_flip_var29 = False
            if v_flip:
                $ yzoom_var29 = round(zoom_var, 2) * -1
                $ v_flip_var29 = True
            if not v_flip:
                $ yzoom_var29 = round(zoom_var, 2)
                $ v_flip_var29 = False
            $ rotate_var29 = rotate_var
            $ xalign_var29 = round(xalign_var, 2)
            $ yalign_var29 = round(yalign_var, 2)
            show expression("[layers[28]]"):
                rotate rotate_var29 xzoom xzoom_var29 yzoom yzoom_var29 xalign xalign_var29 yalign yalign_var29

        if selected_layer == 30:
            if h_flip:
                $ xzoom_var30 = round(zoom_var, 2) * -1
                $ h_flip_var30 = True
            if not h_flip:
                $ xzoom_var30 = round(zoom_var, 2)
                $ h_flip_var30 = False
            if v_flip:
                $ yzoom_var30 = round(zoom_var, 2) * -1
                $ v_flip_var30 = True
            if not v_flip:
                $ yzoom_var30 = round(zoom_var, 2)
                $ v_flip_var30 = False
            $ rotate_var30 = rotate_var
            $ xalign_var30 = round(xalign_var, 2)
            $ yalign_var30 = round(yalign_var, 2)
            show expression("[layers[29]]"):
                rotate rotate_var30 xzoom xzoom_var30 yzoom yzoom_var30 xalign xalign_var30 yalign yalign_var30

        jump image_loop


label restart_layer_counter:
    if selected_layer == 0:
        $ zoom_var = 1.0
        $ xzoom_var = 0.00
        $ yzoom_var = 0.00
        $ xalign_var = 0.00
        $ yalign_var = 0.00
        $ rotate_var = 0
        $ h_flip = False
        $ v_flip = False

    if selected_layer == 1:
        $ zoom_var = xzoom_var1
        $ xzoom_var = xzoom_var1
        $ yzoom_var = yzoom_var1
        $ xalign_var = xalign_var1
        $ yalign_var = yalign_var1
        $ rotate_var = rotate_var1
        $ h_flip = h_flip_var1
        $ v_flip = v_flip_var1
        if h_flip:
            $ zoom_var = xzoom_var1 * - 1
        if v_flip:
            $ zoom_var = yzoom_var1 * - 1

    if selected_layer == 2:
        if layer == 1:
            $ selected_layer = 0
        $ zoom_var = xzoom_var2
        $ xzoom_var = xzoom_var2
        $ yzoom_var = yzoom_var2
        $ xalign_var = xalign_var2
        $ yalign_var = yalign_var2
        $ rotate_var = rotate_var2
        $ h_flip = h_flip_var2
        $ v_flip = v_flip_var2
        if h_flip:
            $ zoom_var = xzoom_var2 * - 1
        if v_flip:
            $ zoom_var = yzoom_var2 * - 1

    if selected_layer == 3:
        if layer == 2:
            $ selected_layer = 0
        $ zoom_var = xzoom_var3
        $ xzoom_var = xzoom_var3
        $ yzoom_var = yzoom_var3
        $ xalign_var = xalign_var3
        $ yalign_var = yalign_var3
        $ rotate_var = rotate_var3
        $ h_flip = h_flip_var3
        $ v_flip = v_flip_var3
        if h_flip:
            $ zoom_var = xzoom_var3 * - 1
        if v_flip:
            $ zoom_var = yzoom_var3 * - 1

    if selected_layer == 4:
        if layer == 3:
            $ selected_layer = 0
        $ zoom_var = xzoom_var4
        $ xzoom_var = xzoom_var4
        $ yzoom_var = yzoom_var4
        $ xalign_var = xalign_var4
        $ yalign_var = yalign_var4
        $ rotate_var = rotate_var4
        $ h_flip = h_flip_var4
        $ v_flip = v_flip_var4
        if h_flip:
            $ zoom_var = xzoom_var4 * - 1
        if v_flip:
            $ zoom_var = yzoom_var4 * - 1

    if selected_layer == 5:
        if layer == 4:
            $ selected_layer = 0
        $ zoom_var = xzoom_var5
        $ xzoom_var = xzoom_var5
        $ yzoom_var = yzoom_var5
        $ xalign_var = xalign_var5
        $ yalign_var = yalign_var5
        $ rotate_var = rotate_var5
        $ h_flip = h_flip_var5
        $ v_flip = v_flip_var5
        if h_flip:
            $ zoom_var = xzoom_var5 * - 1
        if v_flip:
            $ zoom_var = yzoom_var5 * - 1

    if selected_layer == 6:
        if layer == 5:
            $ selected_layer = 0
        $ zoom_var = xzoom_var6
        $ xzoom_var = xzoom_var6
        $ yzoom_var = yzoom_var6
        $ xalign_var = xalign_var6
        $ yalign_var = yalign_var6
        $ rotate_var = rotate_var6
        $ h_flip = h_flip_var6
        $ v_flip = v_flip_var6
        if h_flip:
            $ zoom_var = xzoom_var6 * - 1
        if v_flip:
            $ zoom_var = yzoom_var6 * - 1

    if selected_layer == 7:
        if layer == 6:
            $ selected_layer = 0
        $ zoom_var = xzoom_var7
        $ xzoom_var = xzoom_var7
        $ yzoom_var = yzoom_var7
        $ xalign_var = xalign_var7
        $ yalign_var = yalign_var7
        $ rotate_var = rotate_var7
        $ h_flip = h_flip_var7
        $ v_flip = v_flip_var7
        if h_flip:
            $ zoom_var = xzoom_var7 * - 1
        if v_flip:
            $ zoom_var = yzoom_var7 * - 1

    if selected_layer == 8:
        if layer == 7:
            $ selected_layer = 0
        $ zoom_var = xzoom_var8
        $ xzoom_var = xzoom_var8
        $ yzoom_var = yzoom_var8
        $ xalign_var = xalign_var8
        $ yalign_var = yalign_var8
        $ rotate_var = rotate_var8
        $ h_flip = h_flip_var8
        $ v_flip = v_flip_var8
        if h_flip:
            $ zoom_var = xzoom_var8 * - 1
        if v_flip:
            $ zoom_var = yzoom_var8 * - 1

    if selected_layer == 9:
        if layer == 8:
            $ selected_layer = 0
        $ zoom_var = xzoom_var9
        $ xzoom_var = xzoom_var9
        $ yzoom_var = yzoom_var9
        $ xalign_var = xalign_var9
        $ yalign_var = yalign_var9
        $ rotate_var = rotate_var9
        $ h_flip = h_flip_var9
        $ v_flip = v_flip_var9
        if h_flip:
            $ zoom_var = xzoom_var9 * - 1
        if v_flip:
            $ zoom_var = yzoom_var9 * - 1

    if selected_layer == 10:
        if layer == 9:
            $ selected_layer = 0
        $ zoom_var = xzoom_var10
        $ xzoom_var = xzoom_var10
        $ yzoom_var = yzoom_var10
        $ xalign_var = xalign_var10
        $ yalign_var = yalign_var10
        $ rotate_var = rotate_var10
        $ h_flip = h_flip_var10
        $ v_flip = v_flip_var10
        if h_flip:
            $ zoom_var = xzoom_var10 * - 1
        if v_flip:
            $ zoom_var = yzoom_var10 * - 1

    if selected_layer == 11:
        if layer == 10:
            $ selected_layer = 0
        $ zoom_var = xzoom_var11
        $ xzoom_var = xzoom_var11
        $ yzoom_var = yzoom_var11
        $ xalign_var = xalign_var11
        $ yalign_var = yalign_var11
        $ rotate_var = rotate_var11
        $ h_flip = h_flip_var11
        $ v_flip = v_flip_var11
        if h_flip:
            $ zoom_var = xzoom_var11 * - 1
        if v_flip:
            $ zoom_var = yzoom_var11 * - 1

    if selected_layer == 12:
        if layer == 11:
            $ selected_layer = 0
        $ zoom_var = xzoom_var12
        $ xzoom_var = xzoom_var12
        $ yzoom_var = yzoom_var12
        $ xalign_var = xalign_var12
        $ yalign_var = yalign_var12
        $ rotate_var = rotate_var12
        $ h_flip = h_flip_var12
        $ v_flip = v_flip_var12
        if h_flip:
            $ zoom_var = xzoom_var12 * - 1
        if v_flip:
            $ zoom_var = yzoom_var12 * - 1

    if selected_layer == 13:
        if layer == 12:
            $ selected_layer = 0
        $ zoom_var = xzoom_var13
        $ xzoom_var = xzoom_var13
        $ yzoom_var = yzoom_var13
        $ xalign_var = xalign_var13
        $ yalign_var = yalign_var13
        $ rotate_var = rotate_var13
        $ h_flip = h_flip_var13
        $ v_flip = v_flip_var13
        if h_flip:
            $ zoom_var = xzoom_var13 * - 1
        if v_flip:
            $ zoom_var = yzoom_var13 * - 1

    if selected_layer == 14:
        if layer == 13:
            $ selected_layer = 0
        $ zoom_var = xzoom_var14
        $ xzoom_var = xzoom_var14
        $ yzoom_var = yzoom_var14
        $ xalign_var = xalign_var14
        $ yalign_var = yalign_var14
        $ rotate_var = rotate_var14
        $ h_flip = h_flip_var14
        $ v_flip = v_flip_var14
        if h_flip:
            $ zoom_var = xzoom_var14 * - 1
        if v_flip:
            $ zoom_var = yzoom_var14 * - 1

    if selected_layer == 15:
        if layer == 14:
            $ selected_layer = 0
        $ zoom_var = xzoom_var15
        $ xzoom_var = xzoom_var15
        $ yzoom_var = yzoom_var15
        $ xalign_var = xalign_var15
        $ yalign_var = yalign_var15
        $ rotate_var = rotate_var15
        $ h_flip = h_flip_var15
        $ v_flip = v_flip_var15
        if h_flip:
            $ zoom_var = xzoom_var15 * - 1
        if v_flip:
            $ zoom_var = yzoom_var15 * - 1

    if selected_layer == 16:
        if layer == 15:
            $ selected_layer = 0
        $ zoom_var = xzoom_var16
        $ xzoom_var = xzoom_var16
        $ yzoom_var = yzoom_var16
        $ xalign_var = xalign_var16
        $ yalign_var = yalign_var16
        $ rotate_var = rotate_var16
        $ h_flip = h_flip_var16
        $ v_flip = v_flip_var16
        if h_flip:
            $ zoom_var = xzoom_var16 * - 1
        if v_flip:
            $ zoom_var = yzoom_var16 * - 1

    if selected_layer == 17:
        if layer == 16:
            $ selected_layer = 0
        $ zoom_var = xzoom_var17
        $ xzoom_var = xzoom_var17
        $ yzoom_var = yzoom_var17
        $ xalign_var = xalign_var17
        $ yalign_var = yalign_var17
        $ rotate_var = rotate_var17
        $ h_flip = h_flip_var17
        $ v_flip = v_flip_var17
        if h_flip:
            $ zoom_var = xzoom_var17 * - 1
        if v_flip:
            $ zoom_var = yzoom_var17 * - 1

    if selected_layer == 18:
        if layer == 17:
            $ selected_layer = 0
        $ zoom_var = xzoom_var18
        $ xzoom_var = xzoom_var18
        $ yzoom_var = yzoom_var18
        $ xalign_var = xalign_var18
        $ yalign_var = yalign_var18
        $ rotate_var = rotate_var18
        $ h_flip = h_flip_var18
        $ v_flip = v_flip_var18
        if h_flip:
            $ zoom_var = xzoom_var18 * - 1
        if v_flip:
            $ zoom_var = yzoom_var18 * - 1

    if selected_layer == 19:
        if layer == 18:
            $ selected_layer = 0
        $ zoom_var = xzoom_var19
        $ xzoom_var = xzoom_var19
        $ yzoom_var = yzoom_var19
        $ xalign_var = xalign_var19
        $ yalign_var = yalign_var19
        $ rotate_var = rotate_var19
        $ h_flip = h_flip_var19
        $ v_flip = v_flip_var19
        if h_flip:
            $ zoom_var = xzoom_var19 * - 1
        if v_flip:
            $ zoom_var = yzoom_var19 * - 1

    if selected_layer == 20:
        if layer == 19:
            $ selected_layer = 0
        $ zoom_var = xzoom_var20
        $ xzoom_var = xzoom_var20
        $ yzoom_var = yzoom_var20
        $ xalign_var = xalign_var20
        $ yalign_var = yalign_var20
        $ rotate_var = rotate_var20
        $ h_flip = h_flip_var20
        $ v_flip = v_flip_var20
        if h_flip:
            $ zoom_var = xzoom_var20 * - 1
        if v_flip:
            $ zoom_var = yzoom_var20 * - 1

    if selected_layer == 21:
        if layer == 20:
            $ selected_layer = 0
        $ zoom_var = xzoom_var21
        $ xzoom_var = xzoom_var21
        $ yzoom_var = yzoom_var21
        $ xalign_var = xalign_var21
        $ yalign_var = yalign_var21
        $ rotate_var = rotate_var21
        $ h_flip = h_flip_var21
        $ v_flip = v_flip_var21
        if h_flip:
            $ zoom_var = xzoom_var21 * - 1
        if v_flip:
            $ zoom_var = yzoom_var21 * - 1

    if selected_layer == 22:
        if layer == 21:
            $ selected_layer = 0
        $ zoom_var = xzoom_var22
        $ xzoom_var = xzoom_var22
        $ yzoom_var = yzoom_var22
        $ xalign_var = xalign_var22
        $ yalign_var = yalign_var22
        $ rotate_var = rotate_var22
        $ h_flip = h_flip_var22
        $ v_flip = v_flip_var22
        if h_flip:
            $ zoom_var = xzoom_var22 * - 1
        if v_flip:
            $ zoom_var = yzoom_var22 * - 1

    if selected_layer == 23:
        if layer == 22:
            $ selected_layer = 0
        $ zoom_var = xzoom_var23
        $ xzoom_var = xzoom_var23
        $ yzoom_var = yzoom_var23
        $ xalign_var = xalign_var23
        $ yalign_var = yalign_var23
        $ rotate_var = rotate_var23
        $ h_flip = h_flip_var23
        $ v_flip = v_flip_var23
        if h_flip:
            $ zoom_var = xzoom_var23 * - 1
        if v_flip:
            $ zoom_var = yzoom_var23 * - 1

    if selected_layer == 24:
        if layer == 23:
            $ selected_layer = 0
        $ zoom_var = xzoom_var24
        $ xzoom_var = xzoom_var24
        $ yzoom_var = yzoom_var24
        $ xalign_var = xalign_var24
        $ yalign_var = yalign_var24
        $ rotate_var = rotate_var24
        $ h_flip = h_flip_var24
        $ v_flip = v_flip_var24
        if h_flip:
            $ zoom_var = xzoom_var24 * - 1
        if v_flip:
            $ zoom_var = yzoom_var24 * - 1

    if selected_layer == 25:
        if layer == 24:
            $ selected_layer = 0
        $ zoom_var = xzoom_var25
        $ xzoom_var = xzoom_var25
        $ yzoom_var = yzoom_var25
        $ xalign_var = xalign_var25
        $ yalign_var = yalign_var25
        $ rotate_var = rotate_var25
        $ h_flip = h_flip_var25
        $ v_flip = v_flip_var25
        if h_flip:
            $ zoom_var = xzoom_var25 * - 1
        if v_flip:
            $ zoom_var = yzoom_var25 * - 1

    if selected_layer == 26:
        if layer == 25:
            $ selected_layer = 0
        $ zoom_var = xzoom_var26
        $ xzoom_var = xzoom_var26
        $ yzoom_var = yzoom_var26
        $ xalign_var = xalign_var26
        $ yalign_var = yalign_var26
        $ rotate_var = rotate_var26
        $ h_flip = h_flip_var26
        $ v_flip = v_flip_var26
        if h_flip:
            $ zoom_var = xzoom_var26 * - 1
        if v_flip:
            $ zoom_var = yzoom_var26 * - 1

    if selected_layer == 27:
        if layer == 26:
            $ selected_layer = 0
        $ zoom_var = xzoom_var27
        $ xzoom_var = xzoom_var27
        $ yzoom_var = yzoom_var27
        $ xalign_var = xalign_var27
        $ yalign_var = yalign_var27
        $ rotate_var = rotate_var27
        $ h_flip = h_flip_var27
        $ v_flip = v_flip_var27
        if h_flip:
            $ zoom_var = xzoom_var27 * - 1
        if v_flip:
            $ zoom_var = yzoom_var27 * - 1

    if selected_layer == 28:
        if layer == 27:
            $ selected_layer = 0
        $ zoom_var = xzoom_var28
        $ xzoom_var = xzoom_var28
        $ yzoom_var = yzoom_var28
        $ xalign_var = xalign_var28
        $ yalign_var = yalign_var28
        $ rotate_var = rotate_var28
        $ h_flip = h_flip_var28
        $ v_flip = v_flip_var28
        if h_flip:
            $ zoom_var = xzoom_var28 * - 1
        if v_flip:
            $ zoom_var = yzoom_var28 * - 1

    if selected_layer == 29:
        if layer == 28:
            $ selected_layer = 0
        $ zoom_var = xzoom_var29
        $ xzoom_var = xzoom_var29
        $ yzoom_var = yzoom_var29
        $ xalign_var = xalign_var29
        $ yalign_var = yalign_var29
        $ rotate_var = rotate_var29
        $ h_flip = h_flip_var29
        $ v_flip = v_flip_var29
        if h_flip:
            $ zoom_var = xzoom_var29 * - 1
        if v_flip:
            $ zoom_var = yzoom_var29 * - 1

    if selected_layer == 30:
        if layer == 29:
            $ selected_layer = 0
        $ zoom_var = xzoom_var30
        $ xzoom_var = xzoom_var30
        $ yzoom_var = yzoom_var30
        $ xalign_var = xalign_var30
        $ yalign_var = yalign_var30
        $ rotate_var = rotate_var30
        $ h_flip = h_flip_var30
        $ v_flip = v_flip_var30
        if h_flip:
            $ zoom_var = xzoom_var30 * - 1
        if v_flip:
            $ zoom_var = yzoom_var30 * - 1

    if selected_layer == 31:
        $ selected_layer = 0

    jump image_loop


label layer_diff:
    $ diff_rotate_var2 = round(rotate_var1 - rotate_var2, 2)
    $ diff_rotate_var3 = round(rotate_var2 - rotate_var3, 2)
    $ diff_rotate_var4 = round(rotate_var3 - rotate_var4, 2)
    $ diff_rotate_var5 = round(rotate_var4 - rotate_var5, 2)
    $ diff_rotate_var6 = round(rotate_var5 - rotate_var6, 2)
    $ diff_rotate_var7 = round(rotate_var6 - rotate_var7, 2)
    $ diff_rotate_var8 = round(rotate_var7 - rotate_var8, 2)
    $ diff_rotate_var9 = round(rotate_var8 - rotate_var9, 2)
    $ diff_rotate_var10 = round(rotate_var9 - rotate_var10, 2)
    $ diff_rotate_var11 = round(rotate_var10 - rotate_var11, 2)
    $ diff_rotate_var12 = round(rotate_var11 - rotate_var12, 2)
    $ diff_rotate_var13 = round(rotate_var12 - rotate_var13, 2)
    $ diff_rotate_var14 = round(rotate_var13 - rotate_var14, 2)
    $ diff_rotate_var15 = round(rotate_var14 - rotate_var15, 2)
    $ diff_rotate_var16 = round(rotate_var15 - rotate_var16, 2)
    $ diff_rotate_var17 = round(rotate_var16 - rotate_var17, 2)
    $ diff_rotate_var18 = round(rotate_var17 - rotate_var18, 2)
    $ diff_rotate_var19 = round(rotate_var18 - rotate_var19, 2)
    $ diff_rotate_var20 = round(rotate_var19 - rotate_var20, 2)
    $ diff_rotate_var21 = round(rotate_var20 - rotate_var21, 2)
    $ diff_rotate_var22 = round(rotate_var21 - rotate_var22, 2)
    $ diff_rotate_var23 = round(rotate_var22 - rotate_var23, 2)
    $ diff_rotate_var24 = round(rotate_var23 - rotate_var24, 2)
    $ diff_rotate_var25 = round(rotate_var24 - rotate_var25, 2)
    $ diff_rotate_var26 = round(rotate_var25 - rotate_var26, 2)
    $ diff_rotate_var27 = round(rotate_var26 - rotate_var27, 2)
    $ diff_rotate_var28 = round(rotate_var27 - rotate_var28, 2)
    $ diff_rotate_var29 = round(rotate_var28 - rotate_var29, 2)
    $ diff_rotate_var30 = round(rotate_var29 - rotate_var30, 2)

    $ diff_xalign_var2 = round(xalign_var1 - xalign_var2, 2)
    $ diff_xalign_var3 = round(xalign_var2 - xalign_var3, 2)
    $ diff_xalign_var4 = round(xalign_var3 - xalign_var4, 2)
    $ diff_xalign_var5 = round(xalign_var4 - xalign_var5, 2)
    $ diff_xalign_var6 = round(xalign_var5 - xalign_var6, 2)
    $ diff_xalign_var7 = round(xalign_var6 - xalign_var7, 2)
    $ diff_xalign_var8 = round(xalign_var7 - xalign_var8, 2)
    $ diff_xalign_var9 = round(xalign_var8 - xalign_var9, 2)
    $ diff_xalign_var10 = round(xalign_var9 - xalign_var10, 2)
    $ diff_xalign_var11 = round(xalign_var10 - xalign_var11, 2)
    $ diff_xalign_var12 = round(xalign_var11 - xalign_var12, 2)
    $ diff_xalign_var13 = round(xalign_var12 - xalign_var13, 2)
    $ diff_xalign_var14 = round(xalign_var13 - xalign_var14, 2)
    $ diff_xalign_var15 = round(xalign_var14 - xalign_var15, 2)
    $ diff_xalign_var16 = round(xalign_var15 - xalign_var16, 2)
    $ diff_xalign_var17 = round(xalign_var16 - xalign_var17, 2)
    $ diff_xalign_var18 = round(xalign_var17 - xalign_var18, 2)
    $ diff_xalign_var19 = round(xalign_var18 - xalign_var19, 2)
    $ diff_xalign_var20 = round(xalign_var19 - xalign_var20, 2)
    $ diff_xalign_var21 = round(xalign_var20 - xalign_var21, 2)
    $ diff_xalign_var22 = round(xalign_var21 - xalign_var22, 2)
    $ diff_xalign_var23 = round(xalign_var22 - xalign_var23, 2)
    $ diff_xalign_var24 = round(xalign_var23 - xalign_var24, 2)
    $ diff_xalign_var25 = round(xalign_var24 - xalign_var25, 2)
    $ diff_xalign_var26 = round(xalign_var25 - xalign_var26, 2)
    $ diff_xalign_var27 = round(xalign_var26 - xalign_var27, 2)
    $ diff_xalign_var28 = round(xalign_var27 - xalign_var28, 2)
    $ diff_xalign_var29 = round(xalign_var28 - xalign_var29, 2)
    $ diff_xalign_var30 = round(xalign_var29 - xalign_var30, 2)

    $ diff_yalign_var2 = round(yalign_var1 - yalign_var2, 2)
    $ diff_yalign_var3 = round(yalign_var2 - yalign_var3, 2)
    $ diff_yalign_var4 = round(yalign_var3 - yalign_var4, 2)
    $ diff_yalign_var5 = round(yalign_var4 - yalign_var5, 2)
    $ diff_yalign_var6 = round(yalign_var5 - yalign_var6, 2)
    $ diff_yalign_var7 = round(yalign_var6 - yalign_var7, 2)
    $ diff_yalign_var8 = round(yalign_var7 - yalign_var8, 2)
    $ diff_yalign_var9 = round(yalign_var8 - yalign_var9, 2)
    $ diff_yalign_var10 = round(yalign_var9 - yalign_var10, 2)
    $ diff_yalign_var11 = round(yalign_var10 - yalign_var11, 2)
    $ diff_yalign_var12 = round(yalign_var11 - yalign_var12, 2)
    $ diff_yalign_var13 = round(yalign_var12 - yalign_var13, 2)
    $ diff_yalign_var14 = round(yalign_var13 - yalign_var14, 2)
    $ diff_yalign_var15 = round(yalign_var14 - yalign_var15, 2)
    $ diff_yalign_var16 = round(yalign_var15 - yalign_var16, 2)
    $ diff_yalign_var17 = round(yalign_var16 - yalign_var17, 2)
    $ diff_yalign_var18 = round(yalign_var17 - yalign_var18, 2)
    $ diff_yalign_var19 = round(yalign_var18 - yalign_var19, 2)
    $ diff_yalign_var20 = round(yalign_var19 - yalign_var20, 2)
    $ diff_yalign_var21 = round(yalign_var20 - yalign_var21, 2)
    $ diff_yalign_var22 = round(yalign_var21 - yalign_var22, 2)
    $ diff_yalign_var23 = round(yalign_var22 - yalign_var23, 2)
    $ diff_yalign_var24 = round(yalign_var23 - yalign_var24, 2)
    $ diff_yalign_var25 = round(yalign_var24 - yalign_var25, 2)
    $ diff_yalign_var26 = round(yalign_var25 - yalign_var26, 2)
    $ diff_yalign_var27 = round(yalign_var26 - yalign_var27, 2)
    $ diff_yalign_var28 = round(yalign_var27 - yalign_var28, 2)
    $ diff_yalign_var29 = round(yalign_var28 - yalign_var29, 2)
    $ diff_yalign_var30 = round(yalign_var29 - yalign_var30, 2)

    jump image_loop


label delete_image_move:
    hide expression("[layers[0]]")
    hide expression("[layers[1]]")
    hide expression("[layers[2]]")
    hide expression("[layers[3]]")
    hide expression("[layers[4]]")
    hide expression("[layers[5]]")
    hide expression("[layers[6]]")
    hide expression("[layers[7]]")
    hide expression("[layers[8]]")
    hide expression("[layers[9]]")
    hide expression("[layers[10]]")
    hide expression("[layers[11]]")
    hide expression("[layers[12]]")
    hide expression("[layers[13]]")
    hide expression("[layers[14]]")
    hide expression("[layers[15]]")
    hide expression("[layers[16]]")
    hide expression("[layers[17]]")
    hide expression("[layers[18]]")
    hide expression("[layers[19]]")
    hide expression("[layers[20]]")
    hide expression("[layers[21]]")
    hide expression("[layers[22]]")
    hide expression("[layers[23]]")
    hide expression("[layers[24]]")
    hide expression("[layers[25]]")
    hide expression("[layers[26]]")
    hide expression("[layers[27]]")
    hide expression("[layers[28]]")
    hide expression("[layers[29]]")
    $ layer = 0
    $ layers = []
    $ rotate_var = 0
    $ zoom_var = 1.0
    $ xzoom_var = 0.0
    $ yzoom_var = 0.0
    $ xalign_var = 0.50
    $ yalign_var = 0.50
    $ layer1_active = False
    $ layer2_active = False
    $ layer3_active = False
    $ layer4_active = False
    $ layer5_active = False
    $ layer6_active = False
    $ layer7_active = False
    $ layer8_active = False
    $ layer9_active = False
    $ layer10_active = False
    $ layer11_active = False
    $ layer12_active = False
    $ layer13_active = False
    $ layer14_active = False
    $ layer15_active = False
    $ layer16_active = False
    $ layer17_active = False
    $ layer18_active = False
    $ layer19_active = False
    $ layer20_active = False
    $ layer21_active = False
    $ layer22_active = False
    $ layer23_active = False
    $ layer24_active = False
    $ layer25_active = False
    $ layer26_active = False
    $ layer27_active = False
    $ layer28_active = False
    $ layer29_active = False
    $ layer30_active = False
    $ h_flip = False
    $ v_flip = False
    $ h_flip_var1 = False
    $ v_flip_var1 = False
    $ h_flip_var2 = False
    $ v_flip_var2 = False
    $ h_flip_var3 = False
    $ v_flip_var3 = False
    $ h_flip_var4 = False
    $ v_flip_var4 = False
    $ h_flip_var5 = False
    $ v_flip_var5 = False
    $ h_flip_var6 = False
    $ v_flip_var6 = False
    $ h_flip_var7 = False
    $ v_flip_var7 = False
    $ h_flip_var8 = False
    $ v_flip_var8 = False
    $ h_flip_var9 = False
    $ v_flip_var9 = False
    $ h_flip_var10 = False
    $ v_flip_var10 = False
    $ h_flip_var11 = False
    $ v_flip_var11 = False
    $ h_flip_var12 = False
    $ v_flip_var12 = False
    $ h_flip_var13 = False
    $ v_flip_var13 = False
    $ h_flip_var14 = False
    $ v_flip_var14 = False
    $ h_flip_var15 = False
    $ v_flip_var15 = False
    $ h_flip_var16 = False
    $ v_flip_var16 = False
    $ h_flip_var17 = False
    $ v_flip_var17 = False
    $ h_flip_var18 = False
    $ v_flip_var18 = False
    $ h_flip_var19 = False
    $ v_flip_var19 = False
    $ h_flip_var20 = False
    $ v_flip_var20 = False
    $ h_flip_var21 = False
    $ v_flip_var21 = False
    $ h_flip_var22 = False
    $ v_flip_var22 = False
    $ h_flip_var23 = False
    $ v_flip_var23 = False
    $ h_flip_var24 = False
    $ v_flip_var24 = False
    $ h_flip_var25 = False
    $ v_flip_var25 = False
    $ h_flip_var26 = False
    $ v_flip_var26 = False
    $ h_flip_var27 = False
    $ v_flip_var27 = False
    $ h_flip_var28 = False
    $ v_flip_var28 = False
    $ h_flip_var29 = False
    $ v_flip_var29 = False
    $ h_flip_var30 = False
    $ v_flip_var30 = False
    $ selected_layer = 0
    $ rotate_var1 = 0
    $ rotate_var2 = 0
    $ rotate_var3 = 0
    $ rotate_var4 = 0
    $ rotate_var5 = 0
    $ rotate_var6 = 0
    $ rotate_var7 = 0
    $ rotate_var8 = 0
    $ rotate_var9 = 0
    $ rotate_var10 = 0
    $ rotate_var11 = 0
    $ rotate_var12 = 0
    $ rotate_var13 = 0
    $ rotate_var14 = 0
    $ rotate_var15 = 0
    $ rotate_var16 = 0
    $ rotate_var17 = 0
    $ rotate_var18 = 0
    $ rotate_var19 = 0
    $ rotate_var20 = 0
    $ rotate_var21 = 0
    $ rotate_var22 = 0
    $ rotate_var23 = 0
    $ rotate_var24 = 0
    $ rotate_var25 = 0
    $ rotate_var26 = 0
    $ rotate_var27 = 0
    $ rotate_var28 = 0
    $ rotate_var29 = 0
    $ rotate_var30 = 0
    $ xalign_var1 = 0
    $ xalign_var2 = 0
    $ xalign_var3 = 0
    $ xalign_var4 = 0
    $ xalign_var5 = 0
    $ xalign_var6 = 0
    $ xalign_var7 = 0
    $ xalign_var8 = 0
    $ xalign_var9 = 0
    $ xalign_var10 = 0
    $ xalign_var11 = 0
    $ xalign_var12 = 0
    $ xalign_var13 = 0
    $ xalign_var14 = 0
    $ xalign_var15 = 0
    $ xalign_var16 = 0
    $ xalign_var17 = 0
    $ xalign_var18 = 0
    $ xalign_var19 = 0
    $ xalign_var20 = 0
    $ xalign_var21 = 0
    $ xalign_var22 = 0
    $ xalign_var23 = 0
    $ xalign_var24 = 0
    $ xalign_var25 = 0
    $ xalign_var26 = 0
    $ xalign_var27 = 0
    $ xalign_var28 = 0
    $ xalign_var29 = 0
    $ xalign_var30 = 0
    $ yalign_var1 = 0
    $ yalign_var2 = 0
    $ yalign_var3 = 0
    $ yalign_var4 = 0
    $ yalign_var5 = 0
    $ yalign_var6 = 0
    $ yalign_var7 = 0
    $ yalign_var8 = 0
    $ yalign_var9 = 0
    $ yalign_var10 = 0
    $ yalign_var11 = 0
    $ yalign_var12 = 0
    $ yalign_var13 = 0
    $ yalign_var14 = 0
    $ yalign_var15 = 0
    $ yalign_var16 = 0
    $ yalign_var17 = 0
    $ yalign_var18 = 0
    $ yalign_var19 = 0
    $ yalign_var20 = 0
    $ yalign_var21 = 0
    $ yalign_var22 = 0
    $ yalign_var23 = 0
    $ yalign_var24 = 0
    $ yalign_var25 = 0
    $ yalign_var26 = 0
    $ yalign_var27 = 0
    $ yalign_var28 = 0
    $ yalign_var29 = 0
    $ yalign_var30 = 0
    $ diff_rotate_var2 = 0
    $ diff_rotate_var3 = 0
    $ diff_rotate_var4 = 0
    $ diff_rotate_var5 = 0
    $ diff_rotate_var6 = 0
    $ diff_rotate_var7 = 0
    $ diff_rotate_var8 = 0
    $ diff_rotate_var9 = 0
    $ diff_rotate_var10 = 0
    $ diff_rotate_var11 = 0
    $ diff_rotate_var12 = 0
    $ diff_rotate_var13 = 0
    $ diff_rotate_var14 = 0
    $ diff_rotate_var15 = 0
    $ diff_rotate_var16 = 0
    $ diff_rotate_var17 = 0
    $ diff_rotate_var18 = 0
    $ diff_rotate_var19 = 0
    $ diff_rotate_var20 = 0
    $ diff_rotate_var21 = 0
    $ diff_rotate_var22 = 0
    $ diff_rotate_var23 = 0
    $ diff_rotate_var24 = 0
    $ diff_rotate_var25 = 0
    $ diff_rotate_var26 = 0
    $ diff_rotate_var27 = 0
    $ diff_rotate_var28 = 0
    $ diff_rotate_var29 = 0
    $ diff_rotate_var30 = 0
    $ diff_xalign_var2 = 0
    $ diff_xalign_var3 = 0
    $ diff_xalign_var4 = 0
    $ diff_xalign_var5 = 0
    $ diff_xalign_var6 = 0
    $ diff_xalign_var7 = 0
    $ diff_xalign_var8 = 0
    $ diff_xalign_var9 = 0
    $ diff_xalign_var10 = 0
    $ diff_xalign_var11 = 0
    $ diff_xalign_var12 = 0
    $ diff_xalign_var13 = 0
    $ diff_xalign_var14 = 0
    $ diff_xalign_var15 = 0
    $ diff_xalign_var16 = 0
    $ diff_xalign_var17 = 0
    $ diff_xalign_var18 = 0
    $ diff_xalign_var19 = 0
    $ diff_xalign_var20 = 0
    $ diff_xalign_var21 = 0
    $ diff_xalign_var22 = 0
    $ diff_xalign_var23 = 0
    $ diff_xalign_var24 = 0
    $ diff_xalign_var25 = 0
    $ diff_xalign_var26 = 0
    $ diff_xalign_var27 = 0
    $ diff_xalign_var28 = 0
    $ diff_xalign_var29 = 0
    $ diff_xalign_var30 = 0
    $ diff_yalign_var2 = 0
    $ diff_yalign_var3 = 0
    $ diff_yalign_var4 = 0
    $ diff_yalign_var5 = 0
    $ diff_yalign_var6 = 0
    $ diff_yalign_var7 = 0
    $ diff_yalign_var8 = 0
    $ diff_yalign_var9 = 0
    $ diff_yalign_var10 = 0
    $ diff_yalign_var11 = 0
    $ diff_yalign_var12 = 0
    $ diff_yalign_var13 = 0
    $ diff_yalign_var14 = 0
    $ diff_yalign_var15 = 0
    $ diff_yalign_var16 = 0
    $ diff_yalign_var17 = 0
    $ diff_yalign_var18 = 0
    $ diff_yalign_var19 = 0
    $ diff_yalign_var20 = 0
    $ diff_yalign_var21 = 0
    $ diff_yalign_var22 = 0
    $ diff_yalign_var23 = 0
    $ diff_yalign_var24 = 0
    $ diff_yalign_var25 = 0
    $ diff_yalign_var26 = 0
    $ diff_yalign_var27 = 0
    $ diff_yalign_var28 = 0
    $ diff_yalign_var29 = 0
    $ diff_yalign_var30 = 0
    $ active_layer = ""
    $ image_found = False
    $ image_png_found = False
    $ image_jpg_found = False
    $ image_jpeg_found = False
    $ image_webp_found = False
    $ image_avif_found = False
    $ image_svg_found = False
    $ image_type = []
    hide screen message_delete_layers
    jump image_loop


label continue_game:
    "Under development...{nw=1}"
    ""
    pause(hard = True)


init python:
    def show_date_time():
        try:
            now = datetime.now()
            if now.strftime("%m") == "01":
                month_word = "January"
            if now.strftime("%m") == "02":
                month_word = "February"
            if now.strftime("%m") == "03":
                month_word = "March"
            if now.strftime("%m") == "04":
                month_word = "April"
            if now.strftime("%m") == "05":
                month_word = "May"
            if now.strftime("%m") == "06":
                month_word = "June"
            if now.strftime("%m") == "07":
                month_word = "July"
            if now.strftime("%m") == "08":
                month_word = "August"
            if now.strftime("%m") == "09":
                month_word = "September"
            if now.strftime("%m") == "10":
                month_word = "October"
            if now.strftime("%m") == "11":
                month_word = "November"
            if now.strftime("%m") == "12":
                month_word = "December"
            current_time = now.strftime(month_word + " %d, %Y, %H:%M:%S")
            return current_time
        except Exception as e:
            return f"Error: {e}"


label save_layer_data:
    python:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'layer_positions.txt')
        if layer1_active:
            get_date_time = show_date_time()
            file = open(file_path, "a")
            file.write("\n\n________________________________________________\n")
            file.write("\nLayer data on: " + get_date_time)
            file.write("\n\nLayer 1")
            file.write("\nPath and filename: " + layers[0])
            file.write("\nxzoom: " + str(xzoom_var1))
            file.write("\nyzoom: " + str(yzoom_var1))
            file.write("\nrotate: " + str(rotate_var1))
            file.write("\nxalign: " + str(xalign_var1))
            file.write("\nyalign: " + str(yalign_var1))
            file.write("\nhorizontal flip: " + str(h_flip_var1))
            file.write("\nvertiacl flip: " + str(v_flip_var1))
            file.close()

        if layer2_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 2")
            file.write("\nPath and filename: " + layers[1])
            file.write("\nxzoom: " + str(xzoom_var2))
            file.write("\nyzoom: " + str(yzoom_var2))
            file.write("\nrotate: " + str(rotate_var2))
            file.write("\nxalign: " + str(xalign_var2))
            file.write("\nyalign: " + str(yalign_var2))
            file.write("\nhorizontal flip: " + str(h_flip_var2))
            file.write("\nvertiacl flip: " + str(v_flip_var2))
            file.close()

        if layer3_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 3")
            file.write("\nPath and filename: " + layers[2])
            file.write("\nxzoom: " + str(xzoom_var3))
            file.write("\nyzoom: " + str(yzoom_var3))
            file.write("\nrotate: " + str(rotate_var3))
            file.write("\nxalign: " + str(xalign_var3))
            file.write("\nyalign: " + str(yalign_var3))
            file.write("\nhorizontal flip: " + str(h_flip_var3))
            file.write("\nvertiacl flip: " + str(v_flip_var3))
            file.close()

        if layer4_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 4")
            file.write("\nPath and filename: " + layers[3])
            file.write("\nxzoom: " + str(xzoom_var4))
            file.write("\nyzoom: " + str(yzoom_var4))
            file.write("\nrotate: " + str(rotate_var4))
            file.write("\nxalign: " + str(xalign_var4))
            file.write("\nyalign: " + str(yalign_var4))
            file.write("\nhorizontal flip: " + str(h_flip_var4))
            file.write("\nvertiacl flip: " + str(v_flip_var4))
            file.close()

        if layer5_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 5")
            file.write("\nPath and filename: " + layers[4])
            file.write("\nxzoom: " + str(xzoom_var5))
            file.write("\nyzoom: " + str(yzoom_var5))
            file.write("\nrotate: " + str(rotate_var5))
            file.write("\nxalign: " + str(xalign_var5))
            file.write("\nyalign: " + str(yalign_var5))
            file.write("\nhorizontal flip: " + str(h_flip_var5))
            file.write("\nvertiacl flip: " + str(v_flip_var5))
            file.close()

        if layer6_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 6")
            file.write("\nPath and filename: " + layers[5])
            file.write("\nxzoom: " + str(xzoom_var6))
            file.write("\nyzoom: " + str(yzoom_var6))
            file.write("\nrotate: " + str(rotate_var6))
            file.write("\nxalign: " + str(xalign_var6))
            file.write("\nyalign: " + str(yalign_var6))
            file.write("\nhorizontal flip: " + str(h_flip_var6))
            file.write("\nvertiacl flip: " + str(v_flip_var6))
            file.close()

        if layer7_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 7")
            file.write("\nPath and filename: " + layers[6])
            file.write("\nxzoom: " + str(xzoom_var7))
            file.write("\nyzoom: " + str(yzoom_var7))
            file.write("\nrotate: " + str(rotate_var7))
            file.write("\nxalign: " + str(xalign_var7))
            file.write("\nyalign: " + str(yalign_var7))
            file.write("\nhorizontal flip: " + str(h_flip_var7))
            file.write("\nvertiacl flip: " + str(v_flip_var7))
            file.close()

        if layer8_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 8")
            file.write("\nPath and filename: " + layers[7])
            file.write("\nxzoom: " + str(xzoom_var8))
            file.write("\nyzoom: " + str(yzoom_var8))
            file.write("\nrotate: " + str(rotate_var8))
            file.write("\nxalign: " + str(xalign_var8))
            file.write("\nyalign: " + str(yalign_var8))
            file.write("\nhorizontal flip: " + str(h_flip_var8))
            file.write("\nvertiacl flip: " + str(v_flip_var8))
            file.close()

        if layer9_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 9")
            file.write("\nPath and filename: " + layers[8])
            file.write("\nxzoom: " + str(xzoom_var9))
            file.write("\nyzoom: " + str(yzoom_var9))
            file.write("\nrotate: " + str(rotate_var9))
            file.write("\nxalign: " + str(xalign_var9))
            file.write("\nyalign: " + str(yalign_var9))
            file.write("\nhorizontal flip: " + str(h_flip_var9))
            file.write("\nvertiacl flip: " + str(v_flip_var9))
            file.close()

        if layer10_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 10")
            file.write("\nPath and filename: " + layers[9])
            file.write("\nxzoom: " + str(xzoom_var10))
            file.write("\nyzoom: " + str(yzoom_var10))
            file.write("\nrotate: " + str(rotate_var10))
            file.write("\nxalign: " + str(xalign_var10))
            file.write("\nyalign: " + str(yalign_var10))
            file.write("\nhorizontal flip: " + str(h_flip_var10))
            file.write("\nvertiacl flip: " + str(v_flip_var10))
            file.close()

        if layer11_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 11")
            file.write("\nPath and filename: " + layers[10])
            file.write("\nxzoom: " + str(xzoom_var11))
            file.write("\nyzoom: " + str(yzoom_var11))
            file.write("\nrotate: " + str(rotate_var11))
            file.write("\nxalign: " + str(xalign_var11))
            file.write("\nyalign: " + str(yalign_var11))
            file.write("\nhorizontal flip: " + str(h_flip_var11))
            file.write("\nvertiacl flip: " + str(v_flip_var11))
            file.close()

        if layer12_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 12")
            file.write("\nPath and filename: " + layers[11])
            file.write("\nxzoom: " + str(xzoom_var12))
            file.write("\nyzoom: " + str(yzoom_var12))
            file.write("\nrotate: " + str(rotate_var12))
            file.write("\nxalign: " + str(xalign_var12))
            file.write("\nyalign: " + str(yalign_var12))
            file.write("\nhorizontal flip: " + str(h_flip_var12))
            file.write("\nvertiacl flip: " + str(v_flip_var12))
            file.close()

        if layer13_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 13")
            file.write("\nPath and filename: " + layers[12])
            file.write("\nxzoom: " + str(xzoom_var13))
            file.write("\nyzoom: " + str(yzoom_var13))
            file.write("\nrotate: " + str(rotate_var13))
            file.write("\nxalign: " + str(xalign_var13))
            file.write("\nyalign: " + str(yalign_var13))
            file.write("\nhorizontal flip: " + str(h_flip_var13))
            file.write("\nvertiacl flip: " + str(v_flip_var13))
            file.close()

        if layer14_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 14")
            file.write("\nPath and filename: " + layers[13])
            file.write("\nxzoom: " + str(xzoom_var14))
            file.write("\nyzoom: " + str(yzoom_var14))
            file.write("\nrotate: " + str(rotate_var14))
            file.write("\nxalign: " + str(xalign_var14))
            file.write("\nyalign: " + str(yalign_var14))
            file.write("\nhorizontal flip: " + str(h_flip_var14))
            file.write("\nvertiacl flip: " + str(v_flip_var14))
            file.close()

        if layer15_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 15")
            file.write("\nPath and filename: " + layers[14])
            file.write("\nxzoom: " + str(xzoom_var15))
            file.write("\nyzoom: " + str(yzoom_var15))
            file.write("\nrotate: " + str(rotate_var15))
            file.write("\nxalign: " + str(xalign_var15))
            file.write("\nyalign: " + str(yalign_var15))
            file.write("\nhorizontal flip: " + str(h_flip_var15))
            file.write("\nvertiacl flip: " + str(v_flip_var15))
            file.close()

        if layer16_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 16")
            file.write("\nPath and filename: " + layers[15])
            file.write("\nxzoom: " + str(xzoom_var16))
            file.write("\nyzoom: " + str(yzoom_var16))
            file.write("\nrotate: " + str(rotate_var16))
            file.write("\nxalign: " + str(xalign_var16))
            file.write("\nyalign: " + str(yalign_var16))
            file.write("\nhorizontal flip: " + str(h_flip_var16))
            file.write("\nvertiacl flip: " + str(v_flip_var16))
            file.close()

        if layer17_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 17")
            file.write("\nPath and filename: " + layers[16])
            file.write("\nxzoom: " + str(xzoom_var17))
            file.write("\nyzoom: " + str(yzoom_var17))
            file.write("\nrotate: " + str(rotate_var17))
            file.write("\nxalign: " + str(xalign_var17))
            file.write("\nyalign: " + str(yalign_var17))
            file.write("\nhorizontal flip: " + str(h_flip_var17))
            file.write("\nvertiacl flip: " + str(v_flip_var17))
            file.close()

        if layer18_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 18")
            file.write("\nPath and filename: " + layers[17])
            file.write("\nxzoom: " + str(xzoom_var18))
            file.write("\nyzoom: " + str(yzoom_var18))
            file.write("\nrotate: " + str(rotate_var18))
            file.write("\nxalign: " + str(xalign_var18))
            file.write("\nyalign: " + str(yalign_var18))
            file.write("\nhorizontal flip: " + str(h_flip_var18))
            file.write("\nvertiacl flip: " + str(v_flip_var18))
            file.close()

        if layer19_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 19")
            file.write("\nPath and filename: " + layers[18])
            file.write("\nxzoom: " + str(xzoom_var19))
            file.write("\nyzoom: " + str(yzoom_var19))
            file.write("\nrotate: " + str(rotate_var19))
            file.write("\nxalign: " + str(xalign_var19))
            file.write("\nyalign: " + str(yalign_var19))
            file.write("\nhorizontal flip: " + str(h_flip_var19))
            file.write("\nvertiacl flip: " + str(v_flip_var19))
            file.close()

        if layer20_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 20")
            file.write("\nPath and filename: " + layers[19])
            file.write("\nxzoom: " + str(xzoom_var20))
            file.write("\nyzoom: " + str(yzoom_var20))
            file.write("\nrotate: " + str(rotate_var20))
            file.write("\nxalign: " + str(xalign_var20))
            file.write("\nyalign: " + str(yalign_var20))
            file.write("\nhorizontal flip: " + str(h_flip_var20))
            file.write("\nvertiacl flip: " + str(v_flip_var20))
            file.close()

        if layer21_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 21")
            file.write("\nPath and filename: " + layers[20])
            file.write("\nxzoom: " + str(xzoom_var21))
            file.write("\nyzoom: " + str(yzoom_var21))
            file.write("\nrotate: " + str(rotate_var21))
            file.write("\nxalign: " + str(xalign_var21))
            file.write("\nyalign: " + str(yalign_var21))
            file.write("\nhorizontal flip: " + str(h_flip_var21))
            file.write("\nvertiacl flip: " + str(v_flip_var21))
            file.close()

        if layer22_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 22")
            file.write("\nPath and filename: " + layers[21])
            file.write("\nxzoom: " + str(xzoom_var22))
            file.write("\nyzoom: " + str(yzoom_var22))
            file.write("\nrotate: " + str(rotate_var22))
            file.write("\nxalign: " + str(xalign_var22))
            file.write("\nyalign: " + str(yalign_var22))
            file.write("\nhorizontal flip: " + str(h_flip_var22))
            file.write("\nvertiacl flip: " + str(v_flip_var22))
            file.close()

        if layer23_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 23")
            file.write("\nPath and filename: " + layers[22])
            file.write("\nxzoom: " + str(xzoom_var23))
            file.write("\nyzoom: " + str(yzoom_var23))
            file.write("\nrotate: " + str(rotate_var23))
            file.write("\nxalign: " + str(xalign_var23))
            file.write("\nyalign: " + str(yalign_var23))
            file.write("\nhorizontal flip: " + str(h_flip_var23))
            file.write("\nvertiacl flip: " + str(v_flip_var23))
            file.close()

        if layer24_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 24")
            file.write("\nPath and filename: " + layers[23])
            file.write("\nxzoom: " + str(xzoom_var24))
            file.write("\nyzoom: " + str(yzoom_var24))
            file.write("\nrotate: " + str(rotate_var24))
            file.write("\nxalign: " + str(xalign_var24))
            file.write("\nyalign: " + str(yalign_var24))
            file.write("\nhorizontal flip: " + str(h_flip_var24))
            file.write("\nvertiacl flip: " + str(v_flip_var24))
            file.close()

        if layer25_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 25")
            file.write("\nPath and filename: " + layers[24])
            file.write("\nxzoom: " + str(xzoom_var25))
            file.write("\nyzoom: " + str(yzoom_var25))
            file.write("\nrotate: " + str(rotate_var25))
            file.write("\nxalign: " + str(xalign_var25))
            file.write("\nyalign: " + str(yalign_var25))
            file.write("\nhorizontal flip: " + str(h_flip_var25))
            file.write("\nvertiacl flip: " + str(v_flip_var25))
            file.close()

        if layer26_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 26")
            file.write("\nPath and filename: " + layers[25])
            file.write("\nxzoom: " + str(xzoom_var26))
            file.write("\nyzoom: " + str(yzoom_var26))
            file.write("\nrotate: " + str(rotate_var26))
            file.write("\nxalign: " + str(xalign_var26))
            file.write("\nyalign: " + str(yalign_var26))
            file.write("\nhorizontal flip: " + str(h_flip_var26))
            file.write("\nvertiacl flip: " + str(v_flip_var26))
            file.close()

        if layer27_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 27")
            file.write("\nPath and filename: " + layers[26])
            file.write("\nxzoom: " + str(xzoom_var27))
            file.write("\nyzoom: " + str(yzoom_var27))
            file.write("\nrotate: " + str(rotate_var27))
            file.write("\nxalign: " + str(xalign_var27))
            file.write("\nyalign: " + str(yalign_var27))
            file.write("\nhorizontal flip: " + str(h_flip_var27))
            file.write("\nvertiacl flip: " + str(v_flip_var27))
            file.close()

        if layer28_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 28")
            file.write("\nPath and filename: " + layers[27])
            file.write("\nxzoom: " + str(xzoom_var28))
            file.write("\nyzoom: " + str(yzoom_var28))
            file.write("\nrotate: " + str(rotate_var28))
            file.write("\nxalign: " + str(xalign_var28))
            file.write("\nyalign: " + str(yalign_var28))
            file.write("\nhorizontal flip: " + str(h_flip_var28))
            file.write("\nvertiacl flip: " + str(v_flip_var28))
            file.close()

        if layer29_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 29")
            file.write("\nPath and filename: " + layers[28])
            file.write("\nxzoom: " + str(xzoom_var29))
            file.write("\nyzoom: " + str(yzoom_var29))
            file.write("\nrotate: " + str(rotate_var29))
            file.write("\nxalign: " + str(xalign_var29))
            file.write("\nyalign: " + str(yalign_var29))
            file.write("\nhorizontal flip: " + str(h_flip_var29))
            file.write("\nvertiacl flip: " + str(v_flip_var29))
            file.close()

        if layer30_active:
            file = open(file_path, "a")
            file.write("\n\nLayer 30")
            file.write("\nPath and filename: " + layers[29])
            file.write("\nxzoom: " + str(xzoom_var30))
            file.write("\nyzoom: " + str(yzoom_var30))
            file.write("\nrotate: " + str(rotate_var30))
            file.write("\nxalign: " + str(xalign_var30))
            file.write("\nyalign: " + str(yalign_var30))
            file.write("\nhorizontal flip: " + str(h_flip_var30))
            file.write("\nvertiacl flip: " + str(v_flip_var30))
            file.close()

