# -*- coding: utf-8 -*-
import cocos
import pyglet
import behaviour

from data import NEL_SKILLS,NOD_SKILLS
from battle_data import LEVELS, MONSTERS

class Sprite(cocos.sprite.Sprite):

    def __init__(self,image,position=(0,0)):

        if type(image) == str: 
            image = pyglet.image.load(image)
        
        cocos.sprite.Sprite.__init__(self,image,position, anchor=(image.width/2, 0))
 


class Character(Sprite):

    def __init__(self,name,position=(0,0),code='',lvl=1):

        self.fight_image = None
        self.map_image = None
        self.name = name
        self.box_image = None

        self.dead_image =  None

        try:
            image = pyglet.image.load('img/chara/' + str(name) + '.png')
            self.map_image = image
        except IOError, e:
            image = pyglet.image.load('img/chara/' + str(name) + '-m.png')
            self.map_image = image
            try:
                self.fight_image = pyglet.image.load('img/chara/'+str(name)+'-f.png')

            except IOError, e:
                self.fight_image = self.map_image

            try:
                self.box_image = pyglet.image.load('img/chara/'+str(name)+'-b.png')
            except IOError, e:
                pass

            try:
                self.dead_image = pyglet.image.load('img/chara/'+str(name)+'-mort-f.png')
            except IOError, e:
                if self.fight_image != None:
                    self.dead_image = self.fight_image
                else:
                    self.dead_image = self.map_image

        Sprite.__init__(self,image,position)


        self.map_position = [0,0]
        self.current_map = None

        self.battle_timer = 0.0
        self.battle_threshold = 5.0

        self.in_dialog = False

        self.hpl = [1,1]
        self.hp = 1

        self.mp = 1

        self.level = lvl
        self.set_level(lvl)

        self.mapCode(code)
        self.map_mode()

    def hp():
       
        #doc
        doc = "healt point"
        
        #getter
        def fget(self):

            hp = self.hpl[0]

            return hp
        
        #setter
        def fset(self, hp):
            
            self.hpl[0] = min(hp, self.hpl[1])
            if self.hpl[0] <= 0:
                self.hpl[0] = 0
                print self.hpl
                self.image = self.dead_image

            else:
                self.image = self.fight_image

        #deleter
        def fdel(self):
            pass

        return locals()

    hp = property(**hp())

    def set_level(self,lvl=None):
        if lvl == 'None':
            self.level += 1

        else:
            self.level = lvl

        mp = 0

        if MONSTERS.has_key(self.name):
            hp = MONSTERS[self.name]['hp']

        else:

            hp = LEVELS[self.level]['hp']
            mp = LEVELS[self.level]['mp']

        self.hpl = [hp,hp]
        self.mp = [mp,mp] 



    def is_dead(self,):
        if self.hp <= 0:
            return True
        return False

    def mapCode(self,code):

        if code == 'NEL':
            self.skills =  []
            ne_s = NEL_SKILLS.items()
            ne_s.sort()

            for n,v in ne_s:
                if n <= self.level:
                    self.skills.append(v)

        if code == 'NOD':
            self.skills =  []
            no_s = NOD_SKILLS.items()
            no_s.sort()

            for n,v in no_s:
                if n <= self.level:
                    self.skills.append(v)

    def battle_mode(self):
        
        self.image = self.fight_image
        self.anchor = self.image.width/2, self.image.height/2

    def map_mode(self):

        self.image = self.map_image
        self.anchor = self.image.width/2, self.image.height/2

    def __repr__(self):

        return self.name






