# -*- coding: utf-8 -*-

import cocos
import pyglet
import random

from sprite import Character
from data import ZONE, ENEMY_PROPERTY

class FightScene(cocos.scene.Scene):

    def __init__(self,zone,heros=[]):

        cocos.scene.Scene.__init__(self)

        self.layer = {}

        # battle zone

        self.layer['battle'] = cocos.layer.base_layers.Layer()
        self.add(self.layer['battle'],z=1)


        self.heros = heros

        pos = (650,180)
        for hero in heros:
            self.layer['battle'].add(hero)
            
            hero.position = pos
            hero.battle_mode()

            pos = pos[0] - 55, pos[1] 


        # GUI

        self.layer['gui'] = guiFifhtLayer(self.heros)
        self.add(self.layer['gui'],z=2)

        # BG

        if zone == 'prairie':
            image = pyglet.image.load('img/GUI/bg_prairie.png')
            sprite = cocos.sprite.Sprite(image, anchor=(0,0))
            self.add(sprite,z=0)

        elif zone == 'forest':
            image = pyglet.image.load('img/GUI/bg_forest.png')
            sprite = cocos.sprite.Sprite(image, anchor=(0,0))
            self.add(sprite,z=0)

        #Ennemies

        enemies = ZONE[zone][random.randint(0,len(ZONE[zone])-1)]

        for index in range(len(enemies)):
            enemies[index] = Character(enemies[index])
        
        self.enemies = enemies

        pos = (350,250)

        for enemy in enemies:
            dx, dy = 0,0

            for key,value in ENEMY_PROPERTY.items():
                if enemy.name in value:
                     if key == 'flying':
                        dy += 70


            enemy.position = pos[0] + dx, pos[1] + dy
            pos = pos[0] + 80, pos[1]

            self.layer['battle'].add(enemy)

    def nextHero(self):
        pass

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

        