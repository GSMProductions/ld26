# -*- coding: utf-8 -*-
import cocos
import pyglet
import behaviour

class Sprite(cocos.sprite.Sprite):

    def __init__(self,image,position=(0,0)):

        if type(image) == str: 
            image = pyglet.image.load(image)
        
        cocos.sprite.Sprite.__init__(self,image,position, anchor=(image.width/2, 0))
 


class Character(Sprite):

    def __init__(self,image,position=(0,0),hp=[0,0],mp=[0,0]):

        Sprite.__init__(self,image,position)


        self.map_position = [0,0]
        self.current_map = None

        self.hp = hp
        self.mp = mp






