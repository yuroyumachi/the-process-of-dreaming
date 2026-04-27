
default in_bedroom = True

label bedroom_dialog():
    scene bedroom with dissolve
    player "窗外偶尔传来淅淅沥沥的雨声, 空气里一股潮湿的味道."
    player "可能因为这是春天吧."
    player "很久没有出门了, 也不知道具体情况."
    jump room_bedroom

label room_bedroom:
    scene bedroom
    $ in_bedroom = True
    call screen bedroom()

image bedroom = Composite(
    (1920, 1080),
    (0, 0), Color("#081820"),
    (53 * 8, 72 * 8), "bedroom/bedroom_ground.png",
    (139 * 8, 35 * 8), "bedroom/bedroom_door.png",
    (130 * 8, 27 * 8), "bedroom/bedroom_light_switch.png",
    (52 * 8, 51 * 8), "bedroom/bedroom_desk.png",
    (53 * 8, 77 * 8), "bedroom/bedroom_bed.png",
    (110 * 8, 42 * 8), "player"
)

label real_life_dialog():
    scene real_life with dissolve

    player """
    睡到了天亮,
    突发奇想试试打开房门,
    结果门真的开了.

    鼓起勇气出了门.

    虽然不知道今天为什么想出门, 
    但还是试一试吧.
    """

    show text "{color=#346856}{size=72}唯一的结局(目前的){/size}{/color}":
        # size 72
        xalign 0.5   
        yalign 0.2
    with dissolve
    
    pause

    return

label bedroom_door:
    scene bedroom
    if inventory.is_has_all():
        player """
        门开了
        """
        jump real_life_dialog
    else:
        player "打不开门, 不想出去"
    jump room_bedroom

label bedroom_light_switch:
    scene bedroom
    player "这是灯的开关"
    player "灯在好久之前就坏掉了"
    jump room_bedroom

label bedroom_desk:
    scene bedroom
    player "这是书桌, 靠着窗却没什么光."
    player "书桌上摆着笔记本, 漫画和教辅书,"
    player "我所有的精神食粮."
    menu:
        player "要玩电脑吗"
        "玩电脑":
            call screen computer
        "看书":
            player "光线太暗了, 完全看不了"
        "查看抽屉":
            player "钥匙在很久以前就丢了"
        "不":
            pass
    jump room_bedroom

label bedroom_bed:
    scene bedroom
    menu:
        player "要睡觉吗"
        "睡觉":
            jump room_sleeping
        "不":
            pass
    jump room_bedroom

screen bedroom():
    add "background"

    add "bedroom/bedroom_ground.png":
        xpos 53 * 8
        ypos 72 * 8

    imagebutton:
        xpos 139 * 8
        ypos 35 * 8
        idle "bedroom/bedroom_door.png"
        hover image_brighter("bedroom/bedroom_door.png", 0.2)
        action Jump("bedroom_door")

    imagebutton:
        xpos 130 * 8
        ypos 27 * 8
        idle "bedroom/bedroom_light_switch.png"
        hover image_brighter("bedroom/bedroom_light_switch.png", 0.2)
        action Jump("bedroom_light_switch")

    imagebutton:
        xpos 52 * 8
        ypos 51 * 8
        idle "bedroom/bedroom_desk.png"
        hover image_brighter("bedroom/bedroom_desk.png", 0.2)
        action Jump("bedroom_desk")

    imagebutton:
        xpos 53 * 8
        ypos 77 * 8
        idle "bedroom/bedroom_bed.png"
        hover image_brighter("bedroom/bedroom_bed.png", 0.2)
        action Jump("bedroom_bed")

    imagebutton:
        xpos 187 * 8
        ypos 82 * 8
        idle "right_arrow"
        hover image_brighter("right_arrow", 0.2)
        action Jump("balcony_dialog")

    add "player":
        xpos 110 * 8
        ypos 42 * 8

default is_day = False

label balcony_dialog():

    if inventory.is_has_all():
        scene balcony_real_life with dissolve
        show linkel_real_life:
            pos (132 * 8, 25 * 8)
        player """
        阳台, 这里什么也没有摆放.

        但是有风吹过, 吹过我的脸庞.
        这里用水泥砌的低矮围墙, 让这里围出一片安宁.

        水泥墙之外是另一片光明,
        好像这栋楼就是被光芒拥抱了.

        明日当空, 也万里无云.
        好像这栋楼就是港湾.

        虽然回到室内.
        """
    else:
        scene balcony with dissolve
        show player:
            pos (132 * 8, 25 * 8)
        player """
        阳台, 这里什么也没有摆放.

        没有晾衣架, 没有空调机箱.
        只有用水泥砌的低矮围墙, 让这里看出有点边界.

        水泥墙之外也是一片黑暗,
        好像这栋楼就是被虚无吞没了.

        没有月光, 也看不清云.
        好像这栋楼就是孤舟.

        还是回到室内.
        """

    pause

    jump room_bedroom
