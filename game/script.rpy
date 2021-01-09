# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define narrator = nvl_narrator

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    #объявили каналы аудио для одновременного проигрывания эффектов
    renpy.music.register_channel("channel_1", loop=False)
    renpy.music.register_channel("channel_2", loop=False)

#Splashscreen starts. Раздел для заставки
label splashscreen:
    scene black
    $renpy.pause(2)
    show text "Буланже. Третья республика" with dissolve
    $renpy.pause(4)
    hide text with dissolve
    $renpy.pause(2)
    play music "audio/main_menu_theme.ogg"

    return

# The game starts here. Стартуем игру. Запускаем первую главу

label start:
    stop music fadeout 1.0
    jump chapter_01


#Тестовый комментарий для гитхаба
