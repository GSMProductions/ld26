# -*- coding: utf-8 -*-
from pyglet.window import key
import pyglet
import cocos
from cocos.audio.actions import PlayAction
from dialog import DialogManager
from inventory import Inventory


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
INVENTORY = Inventory()
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

FRIEND_SKILL = ['heal', 'life', 'honey', 'dragon blood', 'potion']

SFX =   {
        'move-select':      pyglet.media.load('sounds/move-select.wav', streaming=False),
        'select':           pyglet.media.load('sounds/select.wav', streaming=False),
        'circles':          pyglet.media.load('sounds/circles.wav', streaming=False),
        'death_monster':    pyglet.media.load('sounds/death_monster.wav', streaming=False),
        'error':            pyglet.media.load('sounds/error.wav', streaming=False),
        'halfsquares':      pyglet.media.load('sounds/halfsquares.wav', streaming=False),
        'heal':             pyglet.media.load('sounds/heal.wav', streaming=False),
        'hit_on_charac':    pyglet.media.load('sounds/hit_on_charac.wav', streaming=False),
        'hit_on_enemies':   pyglet.media.load('sounds/hit_on_enemies.wav', streaming=False),
        'life':             pyglet.media.load('sounds/life.wav', streaming=False),
        'mp':               pyglet.media.load('sounds/regainmp.wav', streaming=False),
        'squares':          pyglet.media.load('sounds/squares.wav', streaming=False),
        'triangles':        pyglet.media.load('sounds/triangles.wav', streaming=False),
        'escape':           pyglet.media.load('sounds/escape.wav', streaming=False)
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
            ('potion', (17,10))
            ],
    'inside_house_gen_1':[
            ('potion', (8,12))
            ],

    'inside_house_gen_2':[
            ('dragon blood', (21,9))
            ],
    'inside_house_gen_3':[
            ],
    'inside_house_gen_4':[
            ],
    'grassland':[
            ('honey', (26,16)),
            ('potion', (37,23)),
            ('stone', (6,11)),
            ('dragon blood', (1,43)),
            ('honey', (22,35))
            ],
    'forest':[
            ('honey', (37,21)),
            ('stone', (14,23)),
            ('dragon blood', (4,38)),
            ('honey', (29,33))
            ],
    'falaise':[
            ]
    }

MAPCHARA = {
    'village1':[
            ('villagera1', (5,38)),
            ('villagerb1', (23,21)),
            ('villagera2', (30,44)),
            ('villagerb2', (6,20)),
            ('villagerb3', (24,21)),
            ('villagerb4', (25,21)),
            ('villagerb5', (43,28)),
            ('villagera3', (5,4)),
            ('villagerb6', (6,4)),
            ('villagera4', (24,36)),
            ('nel11', (33,34))
            ],
    'village2':[
            ('villagera1', (5,38)),
            ('villagerb1', (23,21)),
            ('villagera2', (30,44)),
            ('villagerb2', (6,20)),
            ('villagerb3', (24,21)),
            ('villagerb4', (25,21)),
            ('villagerb5', (43,28)),
            ('villagera3', (5,4)),
            ('villagerb6', (6,4))
            ],            
    'village3':[
            ('villagera1', (22,20)),
            ('villagera2', (21,21)),
            ('villagera3', (28,18)),
            ('villagerb1', (23,17)),
            ('villagerb2', (18,19)),
            ('villagera4', (26,17)),
            ('villagerb3', (23,18)),
            ('villagerb4', (25,18)),
            ('n_the_wise1', (23,21)),
            ('nad21', (24,21)),
            ('nus21', (25,21)),
            ('villagera5', (5,4)),
            ('villagerb5', (6,4))
            ],
    'village4':[
            ('villagera1', (5,38)),
            ('villagera2', (23,21)),
            ('villagera3', (30,44)),
            ('villagerb1', (6,20)),
            ('villagerb2', (24,21)),
            ('villagerb3', (25,21)),
            ('villagerb4', (43,28))
            ],
    'inside_ceremony_hall':[
            ('nad11', (7,8)),
            ('nus11', (20,6))
            ],
    'inside_house_nod':[
            ],
    'inside_house_gen_1':[
            ],
    'inside_house_gen_3':[
            ],
    'inside_house_gen_4':[
            ],
    'inside_house_gen_2':[
            ('villagerb1', (5,8))
             ],
    'grassland':[
            ('dude1', (17,47))
             ],
    'forest':[
            ],
    'falaise':[
            ]
    }

BGM = {
    'village1': 'ld26village.ogg',
    'village2': 'ld26village.ogg',
    'inside_ceremony_hall':'ld26villageindoor.ogg',
    'inside_house_nod':'ld26villageindoor.ogg',
    'inside_house_gen_1':'ld26villageindoor.ogg',
    'inside_house_gen_2':'ld26villageindoor.ogg',
    'inside_house_gen_3':'ld26villageindoor.ogg',
    'inside_house_gen_4':'ld26villageindoor.ogg',
    'grassland':'ld26villageindoor.ogg',
    'forest':'ld26villageindoor.ogg',
    'falaise':'ld26villageindoor.ogg'
    }

TRIGGERS = {
    'village_state':1,
    'found_nel':False
    }