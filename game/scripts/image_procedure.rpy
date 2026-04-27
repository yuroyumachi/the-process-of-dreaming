init python:
    def image_brighter(image: str, brighter: float = 0.2):
        return Transform(image, matrixcolor=BrightnessMatrix(value=brighter))

image right_arrow = "right_arrow.png"
image left_arrow = Transform("right_arrow.png", rotate=180, rotate_pad=False, xanchor=0, yanchor=0)