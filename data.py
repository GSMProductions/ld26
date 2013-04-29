# -*- coding: utf-8 -*-
from pyglet.window import key
import pyglet
import cocos
from cocos.audio.actions import PlayAction
from dialog import DialogManager


TITLE = "Outside The Box"

SCREEN_SIZE = 800,600

TILE_SIZE = 32

ZONE =  {   
        'prairie':       [
                            ['fly','fly'],
                            ['fly','fly'],
                            ['ogre'],
                            ['ogre'],
                            ['ogre','fly','fly']
                        ],
        'forest':       [
                            ['ogre','fly','fly'],
                            ['kraken'],
                            ['ogre','fly','fly'],
                            ['kraken'],
                            ['kraken','fly','fly'],
                            ['dragon']
                        ]  
        }

ENEMY_PROPERTY =    {
                    'flying': ['fly']
                    }
KEYBOARD = key.KeyStateHandler()

MAPS = {}

NOD_SKILLS =    {
                2: 'Heal',
                4: 'Circles',
                6: 'Halfsquares',
                8: 'Life'
                }

NEL_SKILLS =    {
                2: 'Triangles',
                4: 'Squares',
                6: 'Heal',
                8: 'Life'
                }

FRIEND_SKILL = ['heal', 'life']

SFX =   {
        'move-select':    pyglet.media.load('sounds/move-select.wav', streaming=False),
        'select':         pyglet.media.load('sounds/select.wav', streaming=False),
        'circles':        pyglet.media.load('sounds/circles.wav', streaming=False),
        'death_monster':  pyglet.media.load('sounds/death_monster.wav', streaming=False),
        'error':          pyglet.media.load('sounds/error.wav', streaming=False),
        'halfsquares':    pyglet.media.load('sounds/halfsquares.wav', streaming=False),
        'heal':           pyglet.media.load('sounds/heal.wav', streaming=False),
        'hit_on_charac':  pyglet.media.load('sounds/hit_on_charac.wav', streaming=False),
        'hit_on_enemies': pyglet.media.load('sounds/hit_on_enemies.wav', streaming=False),
        'life':           pyglet.media.load('sounds/life.wav', streaming=False),
        'squares':        pyglet.media.load('sounds/squares.wav', streaming=False),
        'triangles':      pyglet.media.load('sounds/triangles.wav', streaming=False),
        'escape':      pyglet.media.load('sounds/escape.wav', streaming=False)
        }

SPEAKERS = {
            'Nod': 'nod1',
            'Nel': 'nel1',
            'Nad': 'nad',
            'N the Wise': 'n_the_wise',
            'Nuss': 'nuss',
            'Dude': 'type_mourant',
            'Villager': 'villager'
           }


DIALOGS = DialogManager()

def mapKey(key):

    if key == pyglet.window.key.SPACE:
        key = pyglet.window.key.ENTER

    elif key == pyglet.window.key.D:
        key = pyglet.window.key.RIGHT

    elif  key == pyglet.window.key.Q or key == pyglet.window.key.A:
        key = pyglet.window.key.LEFT

    elif key == pyglet.window.key.Z or key == pyglet.window.key.W:
        key = pyglet.window.key.UP

    elif key == pyglet.window.key.S:
        key = pyglet.window.key.DOWN

    return key


MAPITEM = {
    'village':[
            ],
    'inside_house_nod':[
            ('potion', (21,47))
            ],
    'inside_house_gen_1':[
            ('potion', (8,48))
            ],

    'inside_house_gen_2':[
            ('dragon blood', (21,43))
            ],
    'grassland':[
            ('honey', (26,23)),
            ('potion', (37,32)),
            ('stone', (3,26)),
            ('dragon blood', (1,52)),
            ('honey', (22,43))
            ],
    'forest':[
            ('honey', (37,28)),
            ('stone', (16,30)),
            ('dragon blood', (4,45)),
            ('honey', (29,40))
            ],
    'falaise':[
            ]
    }

MAPCHARA = {
    'village1':[
            ('villagera', (5,38)),
            ('villagerb', (23,21)),
            ('villagera', (30,44)),
            ('villagerb', (6,20)),
            ('villagerb', (24,21)),
            ('villagerb', (25,21)),
            ('villagerb', (43,28)),
            ('villagera', (5,4)),
            ('villagerb', (6,4))
            ],
    'village2':[
            ('villagera', (22,20)),
            ('villagera', (21,21)),
            ('villagera', (28,18)),
            ('villagerb', (23,17)),
            ('villagerb', (18,19)),
            ('villagera', (26,17)),
            ('villagerb', (23,18)),
            ('villagerb', (25,18)),
            ('n_the_wise', (23,21)),
            ('nad2', (24,21)),
            ('nus2', (25,21)),
            ('villagera', (5,4)),
            ('villagerb', (6,4))
            ],
    'village4':[
            ('villagera', (5,38)),
            ('villagera', (23,21)),
            ('villagera', (30,44)),
            ('villagerb', (6,20)),
            ('villagerb', (24,21)),
            ('villagerb', (25,21)),
            ('villagerb', (43,28))
            ],
    'inside_ceremony_hall':[
            ('nad', (7,49)),
            ('nus', (20,46))
            ],
    'inside_house_nod':[
            ],
    'inside_house_gen_1':[
            ],
    'inside_house_gen_2':[
            ('villagerb', (5,45))
             ],
    'grassland':[
            ('dude', (17,47))
             ],
    'forest':[
            ],
    'falaise':[
            ]
    }
