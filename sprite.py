# -*- coding: utf-8 -*-
import cocos
import pyglet

class Sprite(cocos.sprite.Sprite):

    def __init__(self,image,position=(0,0)):

        if type(image) == str: 
            image = pyglet.image.load(image)
        
        cocos.sprite.Sprite.__init__(self,image,position, anchor=(image.width/2, 0))
 


    def clone(self):

        return Sprite(self.image,self.position)