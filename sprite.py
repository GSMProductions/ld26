# -*- coding: utf-8 -*-
import cocos
import pyglet
import behaviour

from data import NEL_SKILLS,NOD_SKILLS

class Sprite(cocos.sprite.Sprite):

    def __init__(self,image,position=(0,0)):

        if type(image) == str: 
            image = pyglet.image.load(image)
        
        cocos.sprite.Sprite.__init__(self,image,position, anchor=(image.width/2, 0))
 


class Character(Sprite):

    def __init__(self,name,position=(0,0),hp=[0,0],mp=[0,0],lvl=0,code=''):

        self.fight_image = None
        self.map_image = None
        self.name = name

        try:
            image = pyglet.image.load('img/chara/' + str(name) + '.png')
            self.map_image = image
        except IOError, e:
            image = pyglet.image.load('img/chara/' + str(name) + '-m.png')
            self.map_image = image
            try:
                self.fight_image = pyglet.image.load('img/chara/'+str(name)+'-f.png')
            except IOError, e:
                pass

        Sprite.__init__(self,image,position)


        self.map_position = [0,0]
        self.current_map = None

        self.battle_timer = 0.0
        self.battle_threshold = 5.0

        self.hp = hp
        self.mp = mp

        self.level = lvl
        self.mapCode(code)

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

    def map_mode(self):

        self.image = map_image

    def __repr__(self):

        return self.name






