# -*- coding: utf-8 -*-

import cocos
import pyglet
import random

from sprite import Character, Sprite
from data import ZONE, ENEMY_PROPERTY,FRIEND_SKILL, mapKey, SFX


class FightScene(cocos.scene.Scene):

    def __init__(self,zone,heros=[]):

        cocos.scene.Scene.__init__(self)

        self.layer = {}

        # battle zone

        self.layer['battle'] = cocos.layer.base_layers.Layer()
        self.add(self.layer['battle'],z=1)


        self.heros = heros

        pos = (700,180)
        first = True
        heros.reverse()
        for hero in heros:

            if first:
                first = False
                self.active = hero
                self.n_active = 0

            self.layer['battle'].add(hero)
            
            hero.position = pos
            hero.battle_mode()
            hero.hp = hero.hpl[0] # force l'animation de mort

            pos = pos[0] - 90, pos[1]

        heros.reverse()
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

        pos = (200,250)
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
            mvt=None
            enemy.battle_mode()
            pos = pos[0] + enemy.image.width + 20 , pos[1]

            self.layer['battle'].add(enemy)
            

        #arrow

        self.active_arrow = Sprite('img/GUI/arrow_current_character.png')
        self.add(self.active_arrow)
        self.active_arrow.visible = False

        self.next(0)

        # GUI

        self.layer['gui'] = guiFifhtLayer(self.heros,self.enemies)
        self.add(self.layer['gui'],z=2)

        self.bgm = pyglet.media.load("bgm/ld26battle.ogg", streaming=False)
        self.bgm_player = pyglet.media.Player()
        self.bgm_player.queue(self.bgm)
        self.bgm_player.eos_action = self.bgm_player.EOS_LOOP

    def on_enter(self):
        super(FightScene, self).on_enter()
        self.bgm_player.play()

    def on_exit(self):
        self.bgm_player.pause()


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

        if self.active.is_dead():
            self.next()



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
        if self.target.position[1] <= self.begin:
            self.target.velocity = 0,self.speed

        if self.target.position[1] >= self.end:
            self.target.velocity = 0,self.speed * -1



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

    def update_line(self,line,visible=True):
        pc = float(self.skill[0])/self.skill[1]
        w = int(self.width * pc)

        line.end = line.start[0] + w , line.start[1]
        line.visible = visible

    def update(self,visible=True):
        for line in self.lines:
            self.update_line(line,visible)
        


class guiFifhtLayer(cocos.layer.base_layers.Layer):

    def __init__(self,heros=[],enemies=[]):

        cocos.layer.base_layers.Layer.__init__(self)
        image = pyglet.image.load('img/GUI/fight_gui.png')
        sprite = cocos.sprite.Sprite(image,position = (5,5), anchor=(0,0))
        self.add(sprite)

        colorBar = (31,31,31,255)

        self.heros = heros
        self.enemies = enemies

        self.hpbar1 = Bar((14,93),336,self.heros[0].hpl,self)
        self.mpbar1 = Bar((14,68),336,self.heros[0].mp,self)

        self.hpbar2 = Bar((451,93),336,self.heros[1].hpl,self)
        self.mpbar2 = Bar((451,68),336,self.heros[1].mp,self)

        self.schedule(self.callback)

        self.active = 0

        command_l = ['fight','skill','items']

        self.commands = []
        self.commands.append([])
        self.commands.append([])

        self.sub_menu =     [
                            cocos.sprite.Sprite('img/GUI/sub_menu.png',position=(5,5),anchor=(0,0)),
                            cocos.sprite.Sprite('img/GUI/sub_menu.png',position=(404,5),anchor=(0,0))
                            ]

        self.sub_list = []
        self.sub_list.append([])
        self.sub_list.append([])
        
        pos1 = (20,110)
        pos2 = (420,110)

        color = (36,36,36,255)

        for skill in range(4):
            label1 = cocos.text.Label(text='',position = pos1, font_name = 'Statix', color= color , font_size = 20, anchor_x = 'left')
            label2 = cocos.text.Label(text='',position = pos2, font_name = 'Statix', color= color , font_size = 20, anchor_x = 'left')

            label1.visible = False
            label2.visible = False

            pos1 = pos1[0], pos1[1] - 30
            pos2 = pos2[0], pos2[1] - 30

            self.add(label1, z=6)
            self.add(label2, z=6)

            self.sub_list[0].append(label1)
            self.sub_list[1].append(label2)

        self.menu_level = 0
        self.bar_visible = -1

        for menu in self.sub_menu:
            self.add(menu,z=5)
            menu.visible = False


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


        # pour les attaques
        self.attacks = []
        self.action = ''
        self.target =  None
        self.choice_arrow = Sprite('img/GUI/arrow_friend.png')
        self.add(self.choice_arrow,z=6)
        self.choice_arrow.visible = False
        self.n_choice = 0
        self.action_ok =  False


        cocos.director.director.window.push_handlers(self)

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

    def next_slot(self,n=1):

        color = (36,36,36,255)
        selected_color = (197,197,197,255)

        self.n_slot += n

        if self.n_slot >= len(self.sub_list[self.active]):
            self.n_slot = 0

        elif self.n_slot < 0:
            self.n_slot = len(self.sub_list[self.active]) -1


        for cmd in self.sub_list[self.active]:

            cmd.element.color = color

        self.sub_list[self.active][self.n_slot].element.color = selected_color


    def on_key_press(self,key,modifiers):
        return True

    def on_key_release(self,key,modifiers):

        key = mapKey(key)

        if self.menu_level == 0:

            if key == pyglet.window.key.LEFT:
                SFX['move-select'].play()
                self.next_command(-1)

            if key == pyglet.window.key.RIGHT:
                SFX['move-select'].play()
                self.next_command(1)

            if key == pyglet.window.key.ENTER:
                SFX['select'].play()
                self.setMenuLevel(1)

            if key == pyglet.window.key.ESCAPE:
                SFX['error'].play()

        elif self.menu_level == 1:

            if key == pyglet.window.key.UP:
                SFX['move-select'].play()
                self.next_slot(-1)

            if key == pyglet.window.key.DOWN:
                SFX['move-select'].play()
                self.next_slot(1)

            if key == pyglet.window.key.ENTER:
                SFX['select'].play()
                self.action = self.sub_list[self.active][self.n_slot].element.text.lower()

                self.choice_arrow.kill()
                if self.action in FRIEND_SKILL:
                    self.choice_arrow = Sprite('img/GUI/arrow_friend.png')
                else:
                    self.choice_arrow = Sprite('img/GUI/arrow_enemy.png')
                self.add(self.choice_arrow,z=6)

                self.setMenuLevel(2)

            if key == pyglet.window.key.ESCAPE:
                memo = self.n_command
                self.setMenuLevel(0)
                self.n_command = memo

        elif self.menu_level == 2:

            if key == pyglet.window.key.LEFT:
                SFX['move-select'].play()
                self.next_choice(-1)

            if key == pyglet.window.key.RIGHT:
                SFX['move-select'].play()
                self.next_choice(1)

            if key == pyglet.window.key.ENTER:
                SFX['select'].play()
                if self.action in FRIEND_SKILL:
                    self.target = self.heros[self.n_choice]
                else:
                    self.target = self.enemies[self.n_choice]
                self.run_action()

            if key == pyglet.window.key.ESCAPE:
                if self.n_command == 0:
                    self.setMenuLevel(0)
                else:
                    self.setMenuLevel(1)


    def setMenuLevel(self,level):

        self.menu_level =  level


        if self.menu_level == 0:
            self.n_command = 0
            for menu in self.sub_menu:
                menu.visible = False
            self.bar_visible = -1
            self.parent.active_arrow.visible = True

            for l in self.sub_list:
                for label in l:
                    label.visible = False

            self.choice_arrow.visible = False

        elif self.menu_level == 1:
            self.n_slot = 0
            self.parent.active_arrow.visible = True
            if self.n_command == 0:

                self.action = 'fight-hero'

                self.choice_arrow.kill()
                self.choice_arrow = Sprite('img/GUI/arrow_enemy.png')

                self.add(self.choice_arrow,z=6)
                self.setMenuLevel(2)

            if self.n_command == 1 or self.n_command == 1:
                self.choice_arrow.visible = False
                menu = self.sub_menu[self.active]
                menu.visible = True
                self.bar_visible = self.active

                for label in self.sub_list[self.active]:
                    label.visible = True

                if self.n_command == 1:
                    list_skill = self.heros[self.active].skills
     

                    for index in range(len(list_skill)):
                        self.sub_list[self.active][index].element.text = list_skill[index]
                self.next_slot(0)

        elif self.menu_level == 2:
            self.choice_arrow.visible = True
            self.parent.active_arrow.visible = False
            self.n_choice = 0
            self.next_choice()

    def next_choice(self,n=0):

        self.n_choice += n
        if self.action in FRIEND_SKILL:
            end = len(self.heros) - 1
        else:
            end = len(self.enemies) -1

        if self.n_choice < 0:
            self.n_choice = end

        if self.n_choice > end:
            self.n_choice = 0

        if self.action in FRIEND_SKILL:
            pos = self.heros[self.n_choice].position
            pos = pos[0], pos[1] + self.heros[self.n_choice].image.height + 20
            self.choice_arrow.position = pos
        else:
            pos = self.enemies[self.n_choice].position
            pos = pos[0], pos[1] + self.enemies[self.n_choice].image.height + 20
            self.choice_arrow.position = pos


    def callback(self,dt):
        v1 = False
        v2 = False

        if self.bar_visible == 1 or self.bar_visible == -1:
            v1 = True

        if self.bar_visible == 0 or self.bar_visible == -1:
            v2 = True

        self.hpbar1.update(v1)
        self.mpbar1.update(v1)
        self.hpbar2.update(v2)
        self.mpbar2.update(v2)

        ok =  True

        for att in self.attacks:
            if len(att.actions) > 0:
                ok = False
            else:
                att.kill()
                self.attacks.remove(att)

        if ok and self.action_ok:
            self.action_ok = False
            self.parent.next()
            if self.parent.n_active < 2:
                self.active = self.parent.n_active
                self.setMenuLevel(0)
                self.next_command(0)
            else:
                self.next_command(0)
                self.next_command(4)

    def run_action(self):
        self.menu_level = 3
        self.action_ok = True
        origin = self.parent.active

        if self.action == 'triangle':
            pos = self.target.position
            pos = pos[0] -10,  pos[1] - 100
            time = 0.4

            for n in range(3):
                fire = Sprite('img/GUI/fire.png',position = pos)
                self.add(fire,z=7)
                self.attacks.append(fire)
                

                to = self.target.position
                to = pos[0], to[1] + 2*self.target.image.height/3
                action = cocos.actions.interval_actions.MoveTo(to, time)
                SFX['triangles'].play()
                fire.do(action)

                pos = pos[0] + 15, pos[1]
                time += 0.1

        if self.action == 'circle':
            pos = self.target.position
            pos = pos[0], pos[1] + self.target.image.height/2

            img = pyglet.image.load('img/GUI/water.png')
            water = cocos.sprite.Sprite(img,position = pos,anchor = (img.width/2,img.height/2))
            self.add(water,z=7)

            self.attacks.append(water)
            rot = cocos.actions.interval_actions.RotateBy(360,1.)
            sc = cocos.actions.interval_actions.ScaleBy(0.1,1)
            action = rot|sc

            SFX['circles'].play()
            water.do(action)

        elif self.action == 'heal':
            pos = self.target.position
            pos = pos[0], pos[1] + self.target.image.height/2

            img = pyglet.image.load('img/GUI/heal.png')
            heal = cocos.sprite.Sprite(img,position = pos,anchor = (img.width/2,img.height/2))
            self.add(heal,z=7)

            self.attacks.append(heal)
            rot = cocos.actions.interval_actions.RotateBy(-360,0.8)
            sc = cocos.actions.interval_actions.ScaleBy(0.1,0.8)
            action = rot|sc

            SFX['heal'].play()
            heal.do(action)

            if not self.target.is_dead():
                self.target.hp += 10

        elif self.action == 'halfsquares':

            pos = self.target.position
            pos = pos[0],  pos[1] + 300
            time = 0.2

            for n in range(6):
                s = 1
                if n%2 == 0:
                    s = -1

                p = pos[0] + (10 * s), pos[1
                ]
                eclair = Sprite('img/GUI/eclair.png',position = p)
                self.add(eclair,z=7)
                self.attacks.append(eclair)
                

                to = self.target.position
                to = pos[0], to[1] + self.target.image.height/3

                action = cocos.actions.interval_actions.MoveTo(to, time)
                SFX['halfsquares'].play()
                eclair.do(action)

                pos = pos[0] , pos[1] - 15
                time += 0.1

        elif self.action == 'life':

            pos = self.target.position
            pos = pos[0] ,  pos[1]
            time = 0.2

            for n in range(6):


                p = pos[0] , pos[1] + (5 * n%3)

                vie = Sprite('img/GUI/vie.png',position = p)
                self.add(vie,z=7)
                self.attacks.append(vie)
                

                to = self.target.position
                to = pos[0], to[1] + self.target.image.height + 100

                action = cocos.actions.interval_actions.MoveTo(to, time)
                SFX['life'].play()
                vie.do(action)

                pos = pos[0] + 5 , pos[1]
                time += 0.05 * n%2

                if self.target.is_dead:
                    self.target.hp = 5

        elif self.action == 'square':
            pos = self.target.position
            pos = pos[0] ,  pos[1]
            time = 0.2

            for n in range(6):


                p = pos[0] , pos[1] + (10 * n%3)

                earth = Sprite('img/GUI/earth.png',position = p)
                self.add(earth,z=7)
                self.attacks.append(earth)
                

                to = self.target.position
                to = pos[0], to[1] + self.target.image.height + 60

                action = cocos.actions.interval_actions.MoveTo(to, time + n%2 * 0.2)
                SFX['squares'].play()
                earth.do(action)
                pos = pos[0] + 5 , pos[1]

                #time += 0.05 * n%2

        elif self.action == 'fight-hero':

            action = cocos.actions.interval_actions.MoveBy((-10,0),0.2)
            action = action + cocos.actions.base_actions.Reverse(action)

            origin.do(action)









            

        
        
        



        