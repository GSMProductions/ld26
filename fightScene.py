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

        self.layer['gui'] = guiFifhtLayer(self.heros)
        self.add(self.layer['gui'])


class Bar:

    def __init__(self,start,width,skill,parent,):
        
        self.lines = []
        self.width = width
        self.skill = skill

        colorBar = (31,31,31,255)

        for index in range(9):
            start = start[0],start[1] + 1
            end = start[0] + width, start[1]
            
            line = cocos.draw.Line (start,end, color=colorBar, stroke_width=1)
            self.update_line(line)
            self.lines.append(line)
            
            parent.add(line,z=10)

    def update_line(self,line):
        pc = float(self.skill[0])/self.skill[1]
        w = int(self.width * pc)

        line.end = line.start[0] + w , line.start[1]

    def update(self):
        for line in self.lines:
            self.update_line(line)
        




class guiFifhtLayer(cocos.layer.base_layers.Layer):

    def __init__(self,heros=[]):

        cocos.layer.base_layers.Layer.__init__(self)
        image = pyglet.image.load('img/GUI/fight_gui.png')
        sprite = cocos.sprite.Sprite(image,position = (5,5), anchor=(0,0))
        self.add(sprite)

        colorBar = (31,31,31,255)

        self.heros = heros

        self.hpbar1 = Bar((14,93),336,self.heros[0].hp,self)
        self.mpbar1 = Bar((14,68),336,self.heros[0].mp,self)

        self.hpbar2 = Bar((451,93),336,self.heros[1].hp,self)
        self.mpbar2 = Bar((451,68),336,self.heros[1].mp,self)

        self.schedule(self.callback)

    def callback(self,dt):

        self.hpbar1.update()
        self.mpbar1.update()
        self.hpbar2.update()
        self.mpbar2.update()

        