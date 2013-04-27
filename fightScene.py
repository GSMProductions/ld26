# -*- coding: utf-8 -*-

import cocos
import pyglet

from sprite import Sprite

class FightScene(cocos.scene.Scene):

    def __init__(self,heros=[]):

        cocos.scene.Scene.__init__(self)

        self.layer = {}

        # battle zone

        self.layer['battle'] = cocos.layer.base_layers.Layer()
        self.add(self.layer['battle'])


        self.heros = heros

        pos = (650,180)
        for hero in heros:
            self.layer['battle'].add(hero)
            
            hero.position = pos

            pos = pos[0] + 55, pos[1] 


        # GUI

        self.layer['gui'] = guiFifhtLayer()
        self.add(self.layer['gui'])



class guiFifhtLayer(cocos.layer.base_layers.Layer):

    def __init__(self):

        cocos.layer.base_layers.Layer.__init__(self)
        image = pyglet.image.load('img/GUI/fight_gui.png')
        sprite = cocos.sprite.Sprite(image,position = (5,5), anchor=(0,0))
        self.add(sprite)