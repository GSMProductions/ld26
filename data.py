# -*- coding: utf-8 -*-
from pyglet.window import key


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
