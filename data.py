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
            ('potion', (21,9))
            ],
    'inside_house_gen_1':[
            ('potion', (8,8))
            ],

    'inside_house_gen_2':[
            ('dragon blood', (21,13))
            ],
    'grassland':[
            ('honey', (26,33)),
            ('potion', (37,24)),
            ('stone', (3,30)),
            ('dragon blood', (1,4)),
            ('honey', (22,13))
            ],
    'forest':[
            ('honey', (37,28)),
            ('stone', (16,26)),
            ('dragon blood', (4,11)),
            ('honey', (29,16))
            ],
    'falaise':[
            ]
    }

MAPCHARA = {
    'village1':[
            ('villagera', (5,18)),
            ('villagerb', (23,35)),
            ('villagera', (30,12)),
            ('villagerb', (6,36)),
            ('villagerb', (24,35)),
            ('villagerb', (25,35)),
            ('villagerb', (43,28)),
            ('villagera', (5,52)),
            ('villagerb', (6,52))
            ],
    'village2':[
            ('villagera', (22,36)),
            ('villagera', (21,35)),
            ('villagera', (28,38)),
            ('villagerb', (23,39)),
            ('villagerb', (18,37)),
            ('villagera', (26,39)),
            ('villagerb', (23,38)),
            ('villagerb', (25,38)),
            ('n_the_wise', (23,35)),
            ('nad2', (24,35)),
            ('nus2', (25,35)),
            ('villagera', (5,52)),
            ('villagerb', (6,52))
            ],
    'village4':[
            ('villagera', (5,18)),
            ('villagera', (23,35)),
            ('villagera', (30,12)),
            ('villagerb', (6,36)),
            ('villagerb', (24,35)),
            ('villagerb', (25,35)),
            ('villagerb', (43,28))
            ],
    'inside_ceremony_hall':[
            ('nad', (7,7)),
            ('nus', (20,10))
            ],
    'inside_house_nod':[
            ],
    'inside_house_gen_1':[
            ],
    'inside_house_gen_2':[
            ('villagerb', (5,11))
             ],
    'grassland':[
            ('dude', (17,9))
             ],
    'forest':[
            ],
    'falaise':[
            ]
    }
