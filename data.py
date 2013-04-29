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
                            ['ogre','fly','fly'],
                            ['fly','ogre'],
                            ['fly','fly'],
                            ['dragon']
                        ],
        'forest':       [
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
                4: 'Circle',
                6: 'Halfsquares',
                8: 'Life'
                }

NEL_SKILLS =    {
                2: 'Triangle',
                4: 'Square',
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
        'triangles':      pyglet.media.load('sounds/triangles.wav', streaming=False)
        }

SPEAKERS = {
            'Nod': 'nod1',
            'Nel': 'nel1',
            'Nad': 'nad',
            'N the Wise': 'n_the_wise',
            'Nuss': 'nuss',
            'Dude': 'type_mourant'
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


