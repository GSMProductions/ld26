# -*- coding: utf-8 -*-

import cocos
import cocos.scenes
import pyglet

from data import TITLE, SCREEN_SIZE, KEYBOARD, MAPS, DIALOGS,INVENTORY
from fightScene import FightScene
from sprite import Character
from menu import Menu
from map import Map
from behaviour import MoveCharacter, CheckForBattle
from credits import ImgScene
from battle_data import HOOK

def push_credit():
    cr = ImgScene('img/GUI/credits.png')
    cocos.director.director.push(cr)

def push_how_to_play():
    cr = ImgScene('img/GUI/command.png')
    cocos.director.director.push(cr)


def test_combat(zone):
    INVENTORY.add('potion')
    INVENTORY.add('potion')
    INVENTORY.add('dragon blood')
    INVENTORY.add('stone')
    INVENTORY.add('honey')

    heros = [Character('nod1',(0,0),'NOD',1),Character('nel1',(0,0),'NEL',1)]
    dummy_scene = FightScene(zone,heros)
    cocos.director.director.push(dummy_scene)


def start_game():
    INVENTORY.add('potion')
    INVENTORY.add('potion')
    INVENTORY.add('dragon blood')

    HOOK['NED'] = Character('nel1',(0,0),'NEL',1)
    
    player = Character('nod1',(0,0),'NOD',1)
    player.map_mode()
    player.do(MoveCharacter())
    player.do(CheckForBattle())


    MAPS['inside_house_nod'] = Map('inside_house_nod')
    MAPS['village'] = Map('village')
    MAPS['village2'] = Map('village2')
    MAPS['village3'] = Map('village3')

    MAPS['inside_house_gen_1'] = Map('inside_house_gen_1')
    MAPS['inside_house_gen_2'] = Map('inside_house_gen_2')
    MAPS['inside_house_gen_3'] = Map('inside_house_gen_3')
    MAPS['inside_house_gen_4'] = Map('inside_house_gen_4')
    MAPS['inside_ceremony_hall'] = Map('inside_ceremony_hall')
    MAPS['grassland'] = Map('grassland')
    MAPS['forest'] = Map('forest')
    MAPS['falaise'] = Map('falaise')


    MAPS['inside_house_nod'].spawnPlayer(player, (7,9))
    MAPS['inside_house_nod'].displayDialog('Intro')

    cocos.director.director.window.push_handlers(KEYBOARD)
    #cocos.director.director.run(cocos.scenes.FadeTransition(dummy_scene, duration=5))

def callback(dt):
    pyglet.gl.glClearColor(0.85, 0.85, 0.85, 1)

def main():

    #instancification de la fenêtre
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE, do_not_scale=True)
    cocos.director.director.window.pop_handlers()

    logo = pyglet.image.load('img/GUI/icone.png')
    cocos.director.director.window.set_icon(logo)

    pyglet.resource.path.append('font')
    pyglet.resource.path.append('sounds')
    pyglet.resource.reindex()
    pyglet.resource.add_font('Statix.ttf')

    main_command =  [
                    ('Start game',start_game,[]),
                    ('Credits',push_credit,[]),
                    ('Battle (Prairie)',test_combat,['prairie']),
                    ('Battle (Forest)',test_combat,['forest']),
                    ('How to play',push_how_to_play,[])
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
