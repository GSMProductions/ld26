# -*- coding: utf-8 -*-

import cocos
import pyglet

from data import TITLE, SCREEN_SIZE
from fightScene import FightScene
from sprite import Character
from menu import Menu

def test_combat():

    heros = [Character('nod',(0,0),[20,20],[20,20]),Character('nel',(0,0),[20,20],[20,20])]
    dummy_scene = FightScene('prairie',heros)
    cocos.director.director.push(dummy_scene)

def test_map():
    pass

def main():

    #instancification de la fenêtre
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE)

    

    logo = pyglet.image.load('img/GUI/icone.png')
    cocos.director.director.window.set_icon(logo)

    main_command =  [
                    ('Battle Test',test_combat,[]),
                    ('Map Test',test_map,[])
                    ]

    main_scene = cocos.scene.Scene()
    menu =  Menu(main_command)
    main_scene.add(menu)
    cocos.director.director.run(main_scene)

if __name__ == "__main__":
    main()
