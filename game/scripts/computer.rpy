
image computer_background = Composite(
    (1920, 1080),
    (0, 0), Color("#88c070"),
    (0 * 8, 123 * 8), Color("#346856")
)

image computer_timer:
    Text("01:55")
    pause 1.0
    Text("01 55")
    pause 1.0
    repeat

screen computer():
    add "computer_background"

    add "computer_timer":
        xalign 0.5
        yalign 0.5

    frame:
        background None
        xsize 24 * 8
        ysize 32 * 8
        xpos 156 * 8
        ypos 80 * 8
        imagebutton:
            idle "computer_logout.png"
            xfill True
            yfill True
            action Return()
        text "退出":
            xalign 0.5
            yalign 1.0
