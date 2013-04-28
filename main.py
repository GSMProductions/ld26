# -*- coding: utf-8 -*-

import cocos
import cocos.scenes
import pyglet

from data import TITLE, SCREEN_SIZE, KEYBOARD, MAPS
from fightScene import FightScene
from sprite import Character
from menu import Menu
from map import Map
from behaviour import MoveCharacter, CheckForBattle

def test_combat():

    heros = [Character('nod1',(0,0),[20,20],[20,20],10,'NOD'),Character('nel1',(0,0),[20,20],[20,20],10,'NEL')]
    dummy_scene = FightScene('prairie',heros)
    cocos.director.director.push(dummy_scene)

def placeNPCs():

    MAPS['village'].placeCharacter(Character('nuss', (0,0), [0,0], [0,0]), (35,35))



def test_map():
    player = Character('nod1',(0,0),[20,20],[20,20])
    player.do(MoveCharacter())
    player.do(CheckForBattle())



    MAPS['village'] = Map('village')
    MAPS['maptest'] = Map('maptest')

    placeNPCs()


    dummy_scene = MAPS['village']
    dummy_scene.spawnPlayer(player, (30,30))

    cocos.director.director.window.push_handlers(KEYBOARD)
    #cocos.director.director.run(cocos.scenes.FadeTransition(dummy_scene, duration=5))

def callback(dt):
    pyglet.gl.glClearColor(0.85, 0.85, 0.85, 1)

def main():

    #instancification de la fenêtre
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE, do_not_scale=True)

    

    logo = pyglet.image.load('img/GUI/icone.png')
    cocos.director.director.window.set_icon(logo)

    pyglet.resource.path.append('font')
    pyglet.resource.reindex()
    pyglet.resource.add_font('Statix.ttf')

    main_command =  [
                    ('Battle Test',test_combat,[]),
                    ('Map Test',test_map,[])
                    ]

    main_scene = cocos.scene.Scene()
    main_scene.schedule(callback)

    #Title
    sprite = cocos.sprite.Sprite('img/GUI/titre.png',(400,450))
    main_scene.add(sprite)

    menu =  Menu(main_command)
    main_scene.add(menu)
    cocos.director.director.run(main_scene)

if __name__ == "__main__":
    main()
