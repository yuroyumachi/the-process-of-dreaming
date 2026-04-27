
image floor_1_scene_1 = Composite(
    (1920, 1080),
    (0, 0), "background",
    (0, 0), "floor_1/floor_1_ground.png",
    (0, 0), "floor_1/floor_1_wall_for_elevator.png",
    (67 * 8, 11 * 8), "elevator/elevator_door.png",
    (121 * 8, 30 * 8), "elevator/elevator_call.png",
    (114 * 8, 75 * 8), "floor_1/marshmallow_dude.png",
    (42 * 8, 31 * 8), "player",
)

default floor_1_scene_1_first_appear = True
label floor_1_scene_1_dialog():
    scene floor_1_scene_1 with dissolve
    if floor_1_scene_1_first_appear:
        $ button_available = False
        player """
        电梯门外是一条街.
        路上略显昏暗, 但转角和边缘却清晰可见.
        却没有看见任何光源,
        仿佛光是从地面渗出的.

        街上没什么人, 只看到一个先生站在对岸.
        这位先生什么都不做, 只是站在街对岸.

        天气应该很冷, 因为他穿着外套.
        他和我一样, 也是一只猫,
        却没有脸.

        这条街一直延伸至视野尽头.
        后面的场景却像是重复前面的街景.
        """
        $ button_available = True
        $ floor_1_scene_1_first_appear = False

    jump room_floor_1_scene_1

label room_floor_1_scene_1():
    scene floor_1_scene_1

    call screen floor_1_scene_1

label elevator_call():
    scene floor_1_scene_1

    player "实际上这个按钮没有任何用处, 电梯已经在这一层了."

    jump room_floor_1_scene_1

label marshmallow_dude_dialog():
    scene floor_1_scene_1

    if inventory.has("棉花糖"):
        player "这位先生仍然只是站在原地."
    else:
        player """
        我靠近这位站在原地的先生.
        
        他什么话也不说, 手从空中抓取了一些风.
        把风卷成蜘蛛丝, 蛛丝捆成棉花糖.
        
        他把棉花糖递给了我.
        然后再没有其他动作.
        """

        $ inventory.add_item("棉花糖")
        "获得 `棉花糖`"

    jump room_floor_1_scene_1

screen floor_1_scene_1():
    add "background"
    add "floor_1/floor_1_ground.png"
    add "floor_1/floor_1_wall_for_elevator.png"

    imagebutton:
        xpos 67 * 8
        ypos 11 * 8
        idle "elevator/elevator_door.png"
        hover image_brighter("elevator/elevator_door.png", 0.2)
        action Jump("room_elevator")

    imagebutton:
        xpos 121 * 8
        ypos 30 * 8
        idle "elevator/elevator_call.png"
        hover image_brighter("elevator/elevator_call.png", 0.2)
        action Jump("elevator_call")
        
    imagebutton:
        xpos 114 * 8
        ypos 75 * 8
        idle "floor_1/marshmallow_dude.png"
        hover image_brighter("floor_1/marshmallow_dude.png", 0.2)
        action Jump("marshmallow_dude_dialog")

    imagebutton:
        xpos 24 * 8
        ypos 82 * 8
        idle "left_arrow"
        hover image_brighter("left_arrow", 0.2)
        action Jump("marshmallow_dude_dialog")

    imagebutton:
        xpos 187 * 8
        ypos 82 * 8
        idle "right_arrow"
        hover image_brighter("right_arrow", 0.2)
        action Jump("floor_1_scene_2_dialog")

    add "player":
        xpos 42 * 8
        ypos 31 * 8

image floor_1_scene_2 = Composite(
    (1920, 1080),
    (0, 0), "background",
    (0, 0), "floor_1/floor_1_scene_2_ground.png",
    (0, 0), "floor_1/floor_1_scene_2_orange_house.png",
    (211 * 8, 18 * 8), "floor_1/floor_1_trash_can.png",
    (85 * 8, 18 * 8), "floor_1/orange_mouse.png",
    (156 * 8, 33 * 8), "player",
)

default floor_1_scene_2_first_appear = True
label floor_1_scene_2_dialog():
    scene floor_1_scene_2 with dissolve

    if floor_1_scene_2_first_appear:
        $ button_available = False
        player """
        往前走两步,
        就是这条街的另一部分.

        有一位摊贩, 旁边摆满了箱子, 箱子里都是橘子.
        橘子看起来不像橘子, 但是橘子告诉我他们是橘子.

        老板是一只老鼠, 老板没有脸,
        老板穿的是一件背心.

        摊贩附近有一个小巷, 巷里有一个垃圾桶.
        垃圾桶里飘来烟味.
        """
        $ button_available = True

    jump room_floor_1_scene_2

label orange_mouse_dialog():
    scene floor_1_scene_2

    if inventory.has("橘子"):
        player "已经拿过橘子了, 还要拿吗?"
    else:
        player """
        摊贩老板从箱子里拿出一颗橘子.

        隐隐约约能听到箱子里的窃窃私语的声音.

        老板把橘子对着我.
        """
    
    menu:
        player "要拿走橘子吗?"
        "拿走":
            $ inventory.add_item("橘子")
        "不拿":
            pass

    jump room_floor_1_scene_2

label trash_can_dialog():
    scene floor_1_scene_2

    player """
    越是接近巷尾的垃圾桶, 烟味越重.
    
    燃烧的烟, 充斥肺部.

    但是实际看向垃圾桶的内部, 并没有见到堆满的烟头,
    而是几支完好的香烟.
    """

    if inventory.has("橘子"):
        menu:
            player "要拿走一支香烟吗?"
            "是":
                $ inventory.add_item("香烟")
            "否":
                pass
            "丢掉一颗橘子":
                $ inventory.remove_item("橘子")
    else:
        menu:
            player "要拿走一支香烟吗?"
            "是":
                $ inventory.add_item("香烟")
            "否":
                pass

    jump room_floor_1_scene_2

label room_floor_1_scene_2():
    scene floor_1_scene_2

    call screen floor_1_scene_2

screen floor_1_scene_2():
    add "background"
    add "floor_1/floor_1_scene_2_ground.png"
    add "floor_1/floor_1_scene_2_orange_house.png"

    imagebutton:
        pos (211 * 8, 18 * 8)
        idle "floor_1/floor_1_trash_can.png"
        hover image_brighter("floor_1/floor_1_trash_can.png", 0.2)
        action Jump("trash_can_dialog")
    
    imagebutton:
        pos (85 * 8, 18 * 8)
        idle "floor_1/orange_mouse.png"
        hover image_brighter("floor_1/orange_mouse.png", 0.2)
        action Jump("orange_mouse_dialog")

    imagebutton:
        xpos 24 * 8
        ypos 82 * 8
        idle "left_arrow"
        hover image_brighter("left_arrow", 0.2)
        action Jump("floor_1_scene_1_dialog")

    imagebutton:
        xpos 187 * 8
        ypos 82 * 8
        idle "right_arrow"
        hover image_brighter("right_arrow", 0.2)
        action Jump("floor_1_scene_2_dialog")

    add "player":
        pos (156 * 8, 33 * 8)
