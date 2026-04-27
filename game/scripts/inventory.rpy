init python:
    class Item():
        def __init__(self, name, description, function = None)-> None:
            self.name = name
            self.description = description
            self.function = function
        
        def use(self)-> None:
            if self.function != None:
                self.function()

    class Inventory():
        def __init__(self)-> None:
            self._inventory = []
            self._had = set()
            self._selection = ""
            self._is_showing = False

        def on_show(self)-> None:
            self._is_showing = True
            inventory.reset_selection()

        def on_hide(self)-> None:
            self._is_showing = False

        def set_selection(self, name: str)-> None:
            self._selection = name

        def get_selection(self)-> str:
            return self._selection

        def reset_selection(self)-> None:
            self._selection = "manual"
        
        def has(self, name)-> None:
            return name in self._inventory

        def is_has_all(self)-> bool:
            return len(self._had) == len(available_items)

        def get_all_has(self)-> None:
            return self._inventory

        def get_all_items(self)-> None:
            return [self.get_item(item)]

        def add_item(self, name)-> None:
            if name in available_items:
                self._inventory.append(name)
                self._had.add(name)

        def remove_item(self, name)-> None:
            if self.has(name):
                self._inventory.remove(name)

        def get_item(self, name):
            if self.has(name):
                return available_items[name]

        def clear(self)-> None:
            self._inventory.clear()

    def manual_call():
        renpy.call_in_new_context("manual")

    def marshmallow_call():
        global marshmallow_effect
        marshmallow_effect = not marshmallow_effect

    def orange_call():
        inventory.remove_item("橘子")

default marshmallow_effect = False

label tips(msg):
    scene background
    show dialog:
        xsize 0.6
        ysize 0.6
        xalign 0.5
        yalign 0.5
    with dissolve
    play sound tips_sound
    show text msg:
        xalign 0.5
        yalign 0.5
    with dissolve
    pause

    return

label manual():
    scene background with pixellate
    call tips("""卧室里可以在床上进入梦境
在梦里也可以通过捏自己的脸回到现实(按下"数字9")""") from _call_tips
    call tips("""在梦中与各种事件互动有可能会获得一些道具
按下"数字5"可以打开物品栏, 只有在梦中可以使用道具""") from _call_tips_1
    call tips("""本提示可以重新观看
(在物品栏里找到"游戏的说明")""") from _call_tips_2
    scene background with pixellate
    return

default available_items = {
    "游戏的说明" : Item("游戏的说明", "再看一遍游戏的说明", manual_call),
    "棉花糖" : Item("棉花糖", "按下\"使用\"可以装备这件道具, 这将会更改[player_name]的外貌", marshmallow_call),
    "橘子" : Item("橘子", "他在和你说话, \"亲爱的[player_name], 我是一颗橘子, 请吃掉我.\"", orange_call),
    "香烟" : Item("香烟", "很可惜我们的[player_name]并不抽烟"),
}

default inventory = Inventory()

screen inventory_screen():
    zorder 99
    modal True

    on "show" action Function(inventory.on_show)
    on "hide" action Function(inventory.on_hide)
    frame:
        background Frame(image="gui/frame.png", left=15, top=15)
        xsize 0.75
        xalign 0.5
        yalign 0

        if inventory.is_has_all():
            text "现在可以打开卧室的门了.":
                xpos 0.1
                ypos 0.7

        frame:
            background None
            xfill 1
            ysize 0.1
            if inventory.get_item(inventory.get_selection()) == None:
                text "请选择一个物品":
                    xalign 0.1
                    yalign 0.5
            else:
                text inventory.get_item(inventory.get_selection()).description:
                    xalign 0.1
                    yalign 0.5
                if inventory.get_item(inventory.get_selection()).function != None:
                    textbutton "使用":
                        xalign 0.9
                        yalign 0.5
                        action [Hide("inventory_screen"),
                            Function(inventory.get_item(inventory.get_selection()).use)]
        frame:
            background "#346856"
            xsize 0.98
            xalign 0.5
            ypos 0.1
            ysize 5
        frame:
            background None
            xfill 1
            ypos 0.1
            ysize 0.9
            vbox:
                ypos 15
                spacing 15
                xalign 0.2
                for item in inventory.get_all_has():
                    textbutton inventory.get_item(item).name:
                        action Function(inventory.set_selection, inventory.get_item(item).name)

default button_available = True

screen inventory_button():
    
    zorder 100

    if not in_bedroom and button_available:
        button:
            xpos 32
            ypos 32
            if inventory._is_showing:
                action Hide("inventory_screen", transition=dissolve)
            else:
                action Show("inventory_screen", transition=dissolve)

            frame:
                xsize 64
                ysize 64
                text "5":
                    xalign 0.5
                    yalign 0.5

            keysym "5"

screen dream_awake_button():

    zorder 98

    if not in_bedroom and button_available:
        button:
            xpos 128
            ypos 32
            action Jump("dream_awake")

            frame:
                xsize 64
                ysize 64
                text "9":
                    xalign 0.5
                    yalign 0.5

            keysym "9"

label dream_awake():
    scene bedroom with pixellate
    stop music
    $ marshmallow_effect = False
    jump room_bedroom

init python:
    config.overlay_screens.append("inventory_button")
    config.overlay_screens.append("dream_awake_button")
