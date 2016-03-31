from pyglet import font
from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite


class PlayerLayer(Layer):

    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.player = pyglet.resource.image('Assets/AtmoFlight/Trash-Jet.png')
        self.player.anchor_x = self.player.width // 2
        self.player.anchor_y = self.player.height // 2
        self.sprite1 = Sprite(self.player)
        self.add(self.sprite1)
        self.sprite1.position = 320, 300


class PlayerMoveTo(PlayerLayer):

    def on_enter(self):
        super().on_enter()
        self.sprite1.do(MoveTo((620, 300), 4))

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.sprite1.do(MoveTo((x, y), 2))

    def on_key_press(self, k, m):
        posX, posY = self.sprite1.position
        if k == key.LEFT:
            self.sprite1.do(MoveTo((posX - 20, posY), .5))
        elif k == key.RIGHT:
            self.sprite1.do(MoveTo((posX + 20, posY), .5))
        elif k == key.UP:
            self.sprite1.do(MoveTo((posX, posY + 20), .5))
        elif k == key.DOWN:
            self.sprite1.do(MoveTo((posX, posY - 20), .5))

if __name__ == "__main__":
    director.init(resizable=True, caption='A Start')
    director.run(Scene(PlayerMoveTo()))