# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Example 01', color="#c8ffc8")



# The game starts here.
label start:
    style blackboard_style is text:
        color "#FFFFFF"
        size 32
        font "fonts/BadGong.ttf"

    transform blackboard_tl:
        size (208,130)
        on show:
            yalign 0.293 xalign 0.385

    image blackboard = ParameterizedText(xalign=0.425, yalign=0.35, style="blackboard_style")
    image linChalk = Image("lin-chalk-original.webp")
    image bg_lobby = Image("bg-lobby.webp")
    image bg_lobby_original = Image("bg-lobby-original.webp")
    image lin_chalk = Image("lin-chalk-no-text.webp")
    image lin_chalk_original = Image("lin-chalk-original.webp")

    scene bg_lobby_original
    e "Test step 1: the lobby without any overlay text"

    scene bg_lobby
    e "Test step 2: the lobby with blured blackboard"

    show lin_chalk_original at blackboard_tl
    e "Test step 3: the lobby with lin on the blackboard (text is part of the image)"

    hide lin_chalk_original
    show lin_chalk at blackboard_tl
    e "Test step 4: the lobby with lin on the blackboard (clean image)"

    show blackboard "  6:00am\n12:00am"
    e "Test step 4: the lobby with lin and text on the blackboard"

    return
