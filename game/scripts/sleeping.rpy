
label room_sleeping():
    scene sleeping
    call screen sleeping()

image sleeping = Composite(
    (1920, 1080),
    (0, 0), Color("#081820"),
    (89 * 8, 21 * 8), "sleeping_on_the_bed.png"
)

image counting:
    "#0000"
    pause 0.5
    "count_3.png"
    pause 1.0
    "count_2.png"
    pause 1.0
    "count_1.png"

transform counter:
    alpha 0.0
    pause 0.5
    block:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat

screen sleeping():
    add "sleeping"
    frame:
        background None
        add "counter.png" at counter:
            xpos 48 * 8
            ypos 24 * 8
        add "counting":
            xpos 63 * 8
            ypos 27 * 8

    button:
        xfill True
        yfill True
        action Jump("room_bedroom")

    timer 3.5 action [ SetVariable("in_bedroom", False),
        Jump("dream_bedroom_dialog")
        ]
