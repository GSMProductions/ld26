# -*- coding: utf-8 -*-

import cocos
import pyglet
from data import mapKey


class CreditScene(cocos.scene.Scene):

    def __init__(self):

        cocos.scene.Scene.__init__(self)

        layer = cocos.layer.Layer()
        image =  pyglet.image.load('img/GUI/credits.png')
        sprite = cocos.sprite.Sprite(image,(0,0),anchor=(0,0))
        layer.add(sprite)
        self.add(layer)

        cocos.director.director.window.push_handlers(self)

    def on_key_press(self,key,modifiers):
        return True

    def on_key_release(self,key,modifiers):

        key = mapKey(key)

        if key == pyglet.window.key.ESCAPE:
            cocos.director.director.window.pop_handlers()
            self.end()