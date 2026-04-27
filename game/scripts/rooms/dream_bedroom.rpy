
label dream_bedroom_dialog():
    scene dream_bedroom with dissolve
    play music dream_bedroom fadein 1.0 fadeout 1.0
    jump room_dream_bedroom

label room_dream_bedroom():
    scene dream_bedroom
    call screen dream_bedroom()

label dream_bedroom_light_switch():
    scene dream_bedroom
    player "这是灯的开关,{p}灯依旧是坏的."
    jump room_dream_bedroom

label dream_bedroom_desk():
    scene dream_bedroom
    player "这是书桌."
    menu:
        player "要玩电脑吗?"
        "玩电脑":
            stop music fadeout 1.0
            call screen dream_computer
            jump dream_bedroom_dialog
        "看书":
            player "随手拿起一本书, 勉强看清标题上有一个\"二\"的字样."
            player "里面有一句话: \"无论今后的人生有多么坎坷....\""
            player "根本没看明白, 应该是某一系列的励志向作品吧."
        "查看抽屉":
            player "抽屉里是我的倒影."
        "不":
            pass
    jump room_dream_bedroom

image dream_bedroom = Composite(
    (1920, 1080),
    (0, 0), Color("#081820"),
    (53 * 8, 72 * 8), "bedroom/bedroom_ground.png",
    (139 * 8, 35 * 8), "bedroom/bedroom_door.png",
    (130 * 8, 27 * 8), "bedroom/bedroom_light_switch.png",
    (52 * 8, 51 * 8), "bedroom/bedroom_desk.png",
    (110 * 8, 42 * 8), "player"
)

image dream_computer_timer:
    Text("23:65", color="#346856")
    pause 1.0
    Text("23 65", color="#346856")
    pause 1.0
    repeat

screen dream_computer():
    add "background"

    add "dream_computer_timer":
        xalign 0.9
        yalign 0.2

    add "dream_computer_goat.png":
        xpos 54 * 8
        ypos 31 * 8

    imagebutton:
        xpos 194 * 8
        ypos 46 * 8
        idle "dream_computer_logout.png"
        action Return()

screen dream_bedroom():
    add "background"

    add "bedroom/bedroom_ground.png":
        xpos 53 * 8
        ypos 72 * 8

    imagebutton:
        xpos 139 * 8
        ypos 35 * 8
        idle "bedroom/bedroom_door.png"
        hover image_brighter("bedroom/bedroom_door.png", 0.2)
        action [
            Function(elevator_control.set_current_floor, 4),
            Jump("room_elevator")
            ]

    imagebutton:
        xpos 130 * 8
        ypos 27 * 8
        idle "bedroom/bedroom_light_switch.png"
        hover image_brighter("bedroom/bedroom_light_switch.png", 0.2)
        action Jump("dream_bedroom_light_switch")

    imagebutton:
        xpos 52 * 8
        ypos 51 * 8
        idle "bedroom/bedroom_desk.png"
        hover image_brighter("bedroom/bedroom_desk.png", 0.2)
        action Jump("dream_bedroom_desk")

    add "player":
        xpos 110 * 8
        ypos 42 * 8

