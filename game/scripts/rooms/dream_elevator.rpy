
init python:
    class Elevator:
        def __init__(self)-> None:
            self.current_floor = 4
            self.new_floor = 0
        
        def get_current_floor(self)-> int:
            return self.current_floor

        def set_current_floor(self, target_floor: int)-> None:
            self.current_floor = target_floor

        def update_floor(self)-> None:
            self.current_floor = self.new_floor
            self.new_floor = 0

        def goto_floor(self, target_floor: int)-> None:
            if self.get_current_floor() == target_floor:
                renpy.jump("room_elevator")
            else:
                self.new_floor = target_floor
                renpy.jump("running_elevator")
                
default elevator_control = Elevator()

image elevator = Composite(
    (1920, 1080),
    (0, 0), Color("#081820"),
    (75 * 8, 78 * 8), "elevator/elevator_ground.png",
    (91 * 8, 26 * 8), "elevator/elevator_door.png",
    (140 * 8, 42 * 8), "elevator/elevator_floor_selector.png",
    (93 * 8, 15 * 8), "elevator_floor_sign",
    (76 * 8, 44 * 8), "player"
)

image elevator_floor_sign = ConditionSwitch(
    "elevator_control.get_current_floor() == 1", "elevator/elevator_floor_sign_1.png",
    "elevator_control.get_current_floor() == 2", "elevator/elevator_floor_sign_2.png",
    "elevator_control.get_current_floor() == 3", "elevator/elevator_floor_sign_3.png",
    "elevator_control.get_current_floor() == 4", "elevator/elevator_floor_sign_4.png",
)

transform elevator_shaking:
    parallel:
        linear 0.1 xoffset 0
        linear 0.1 xoffset 5
        linear 0.1 xoffset -5
        repeat
    parallel:
        linear 0.1 yoffset 0
        linear 0.02 yoffset 3
        linear 0.02 yoffset -3
        repeat

label running_elevator():
    scene background with dissolve
    show elevator with dissolve
    show elevator at elevator_shaking
    play music elevator_running
    pause 2.0
    stop music
    play sound elevator_beep
    $ elevator_control.update_floor()

    jump room_elevator

label room_elevator():
    scene elevator with dissolve
    # show elevator with dissolve
    stop music fadeout 1.0

    show elevator_floor_sign:
        xpos 93 * 8
        ypos 15 * 8
    with dissolve

    call screen elevator()

label floor_not_available():
    player "电梯门打不开"

    jump room_elevator

screen elevator():
    add "background"

    add "elevator/elevator_ground.png":
        xpos 75 * 8
        ypos 78 * 8

    imagebutton:
        xpos 91 * 8
        ypos 26 * 8
        idle "elevator/elevator_door.png"
        hover image_brighter("elevator/elevator_door.png", 0.2)
        if elevator_control.get_current_floor() == 4:
            action Jump("dream_bedroom_dialog")
        elif elevator_control.get_current_floor() == 3:
            action Jump("floor_not_available")
        elif elevator_control.get_current_floor() == 2:
            action Jump("floor_not_available")
        elif elevator_control.get_current_floor() == 1:
            action Jump("floor_1_scene_1_dialog")
            
    imagebutton:
        xpos 140 * 8
        ypos 42 * 8
        idle "elevator/elevator_floor_selector.png"
        hover image_brighter("elevator/elevator_floor_selector.png", 0.2)
        action Jump("elevator_selector")

    if elevator_control.get_current_floor() == 1:
        add "elevator/elevator_floor_sign_1.png":
            xpos 93 * 8
            ypos 15 * 8
    elif elevator_control.get_current_floor() == 2:
        add "elevator/elevator_floor_sign_2.png":
            xpos 93 * 8
            ypos 15 * 8
    elif elevator_control.get_current_floor() == 3:
        add "elevator/elevator_floor_sign_3.png":
            xpos 93 * 8
            ypos 15 * 8
    elif elevator_control.get_current_floor() == 4:
        add "elevator/elevator_floor_sign_4.png":
            xpos 93 * 8
            ypos 15 * 8

    add "player":
        xpos 76 * 8
        ypos 44 * 8

image elevator_selector_scene_image = Composite(
    (1920, 1080),
    (0, 0), Color("#081820"),
    (0, 0), "elevator/elevator_selector_interface.png",
    (136 * 8, 32 * 8), "elevator/elevator_selector_button_4.png",
    (136 * 8, 51 * 8), "elevator/elevator_selector_button_3.png",
    (136 * 8, 70 * 8), "elevator/elevator_selector_button_2.png",
    (136 * 8, 89 * 8), "elevator/elevator_selector_button_1.png"
)


label elevator_selector:
    scene elevator_selector_scene_image with dissolve

    call screen elevator_selector

screen elevator_selector():
    add "background"
    
    add "elevator/elevator_selector_interface.png"

    imagebutton:
        xpos 136 * 8
        ypos 32 * 8
        idle "elevator/elevator_selector_button_4.png"
        hover image_brighter("elevator/elevator_selector_button_4.png", 0.2)
        action Function(elevator_control.goto_floor, 4)
    
    imagebutton:
        xpos 136 * 8
        ypos 51 * 8
        idle "elevator/elevator_selector_button_3.png"
        hover image_brighter("elevator/elevator_selector_button_3.png", 0.2)
        action Function(elevator_control.goto_floor, 3)

    imagebutton:
        xpos 136 * 8
        ypos 70 * 8
        idle "elevator/elevator_selector_button_2.png"
        hover image_brighter("elevator/elevator_selector_button_2.png", 0.2)
        action Function(elevator_control.goto_floor, 2)

    imagebutton:
        xpos 136 * 8
        ypos 89 * 8
        idle "elevator/elevator_selector_button_1.png"
        hover image_brighter("elevator/elevator_selector_button_1.png", 0.2)
        action Function(elevator_control.goto_floor, 1)
