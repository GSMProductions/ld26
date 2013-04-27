# -*- coding: utf-8 -*-

import cocos
import pyglet
import random

from sprite import Character, Sprite
from data import ZONE, ENEMY_PROPERTY, mapKey


class FightScene(cocos.scene.Scene):

    def __init__(self,zone,heros=[]):

        cocos.scene.Scene.__init__(self)

        self.layer = {}

        # battle zone

        self.layer['battle'] = cocos.layer.base_layers.Layer()
        self.add(self.layer['battle'],z=1)


        self.heros = heros

        pos = (650,180)
        first = True

        for hero in heros:

            if first:
                first = False
                self.active = hero
                self.n_active = 0

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

        str_enemies = ZONE[zone][random.randint(0,len(ZONE[zone])-1)]
        enemies = []
        for index in range(len(str_enemies)):
            enemies.append(Character(str_enemies[index]))
        
        self.enemies = enemies

        pos = (350,250)
        mvt = None

        for enemy in enemies:
            dx, dy = 0,0

            for key,value in ENEMY_PROPERTY.items():
                if enemy.name in value:
                     if key == 'flying':
                        dy += 70
                        mvt = UpAndDown(10,10)

            enemy.position = pos[0] + dx, pos[1] + dy
            if mvt != None:
                enemy.do(mvt)

            pos = pos[0] + 80, pos[1]

            self.layer['battle'].add(enemy)

        #arrow

        self.active_arrow = Sprite('img/GUI/arrow_current_character.png')
        self.add(self.active_arrow)
        self.active_arrow.visible = False

        self.next(0)


    def next(self,index=None):

        #selection
        if index != None:
            self.n_active = index
        else:
            self.n_active += 1

        if self.n_active >= len(self.heros):
            #ennemies
            n = self.n_active - len(self.heros)
            if n >= len(self.enemies):
                self.n_active = 0
                self.active = self.heros[0]
            else:
                self.active = self.enemies[n]
        else:
            self.active = self.heros[self.n_active]

        pos = self.active.position

        pos = pos[0], pos[1] + self.active.image.height + 15

        self.active_arrow.visible = True
        self.active_arrow.position = pos



class UpAndDown(cocos.actions.move_actions.Move):

    def init(self,*args,**kwargs):

        cocos.actions.move_actions.Move.init(self)
        self.speed = args[0]
        self.height = args[1]
        

    def start(self):
        cocos.actions.move_actions.Move.start(self)

        y = self.target.position[1]

        self.begin = y - self.height/2
        self.end = y + self.height/2

        self.target.velocity = 0,self.speed


    def step(self,dt):

        cocos.actions.move_actions.Move.step(self,dt)
        if self.target.position[1] <= self.begin or self.target.position[1] >= self.end:
            self.target.velocity = self.target.velocity[0], self.target.velocity[1] * -1



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

        self.active = 0

        command_l = ['fight','skill','items']

        self.commands = []
        self.commands.append([])
        self.commands.append([])
        

        pos = (420,13)
        color = (36,36,36,255)
        selected_color = (197,197,197,255)


        for cmd in command_l:
            label = cocos.text.Label(text=cmd,position = pos, font_name = 'Statix', color= color , font_size = 20, anchor_x = 'left')
            self.add(label,z=2)
            self.commands[1].append(label)
        
            pos = pos[0]+ 60, pos[1]

        pos = (210,13)

        for cmd in command_l:
            label = cocos.text.Label(text=cmd,position = pos, font_name = 'Statix', color= color , font_size = 20, anchor_x = 'left')
            self.add(label,z=2)
            self.commands[0].append(label)
        
            pos = pos[0]+ 60, pos[1]

        self.n_command = 0
        self.next_command(0)

    def next_command(self,n=1):

        color = (36,36,36,255)
        selected_color = (197,197,197,255)

        self.n_command += n

        if self.n_command >= len(self.commands[self.active]):
            self.n_command = 0

        elif self.n_command < 0:
            self.n_command = len(self.commands[self.active]) -1


        for cmd in self.commands[0]+self.commands[1]:

            cmd.element.color = color

        self.commands[self.active][self.n_command].element.color = selected_color

        cocos.director.director.window.push_handlers(self)


    def on_key_release(self,key,modifiers):

        key = mapKey(key)

        if key == pyglet.window.key.LEFT:
            self.next_command(-1)

        if key == pyglet.window.key.RIGHT:
            self.next_command(1)


    def callback(self,dt):

        self.hpbar1.update()
        self.mpbar1.update()
        self.hpbar2.update()
        self.mpbar2.update()

        