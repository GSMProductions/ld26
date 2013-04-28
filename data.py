# -*- coding: utf-8 -*-
from pyglet.window import key
import pyglet


TITLE = "Outside The Box"

SCREEN_SIZE = 800,600

TILE_SIZE = 32

ZONE =  {   
        'prairie':       [
                            ['ogre','fly','fly'],
                            ['fly','ogre'],
                            ['fly','fly'],
                            ['dragon']
                        ],
        'forest':       [
                        ]  
        }

ENEMY_PROPERTY =    {
                    'flying': ['fly']
                    }
KEYBOARD = key.KeyStateHandler()

MAPS = {}

NOD_SKILLS =    {
                1: 'TRIANGLE MAGIC',
                2: 'SQUARE MAGIC',
                3: 'CIRCLE MAGIC',
                4: 'LINE MAGIC'
                }

NEL_SKILLS =    {
                1: 'TEST MAGIC',
                2: 'SQUARE MAGIC',
                3: 'CIRCLE MAGIC',
                4: 'LINE MAGIC'
                }

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

