
image player_head = ConditionSwitch(
    "in_bedroom", "linkel/linkel_head.png",
    "marshmallow_effect", "linkel/linkel_head_marshmallow.png",
    "True", "linkel/linkel_head.png",
)

image player_body = "linkel/linkel_body.png"

image player = Composite(
    (42 * 8, 19 * 8),
    (0, 0), "player_head",
    (0, 0), "player_body"
)
