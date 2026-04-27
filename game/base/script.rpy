
define player = Character("[player_name]", image="player")

image black = Color("#000000")
image white = Color("#ffffff")
image background = Color("#081820")
image dialog = Frame("gui/frame.png")

label start:

    scene black with fade
    "{color=#ff9900}警告: 在此游戏中可能会有\n令玩家感到不安的场景,\n也可能是我多虑了....{/color}"
    scene black with dissolve
    pause 1.0
    scene another_escape with dissolve
    pause 2.0
    scene background with dissolve

    $ name_confirmed = False
    while not name_confirmed:
        "在开始今晚的梦之前, 请为你的角色命名(默认是 Linkel){nw}"
        python:
            player_name = renpy.input("在开始今晚的梦之前, 请为你的角色命名(默认是 Linkel)")
            player_name = player_name.strip()
            if player_name == "":
                player_name = "Linkel"

        menu:
            player "是这个名字没错吗"
            "没错":
                $ name_confirmed = True
            "不对":
                pass
    $ del name_confirmed

    "{cps=7}好的.{/cps}"
    "{cps=16}欢迎, [player_name]{/cps}"

    call manual() from _call_manual
    $ inventory.add_item("游戏的说明")

    scene background with dissolve
    show title:
        xalign 0.5
        ypos 42 * 8
    with dissolve
    pause 3.0

    jump bedroom_dialog

    return
