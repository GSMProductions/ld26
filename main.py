# -*- coding: utf-8 -*-

import cocos

from data import TITLE, SCREEN_SIZE
from fightScene import FightScene
from sprite import Sprite

def main():

    #instancification de la fenêtre
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE)

    heros = [Sprite('img/chara/nod-f.png'),Sprite('img/chara/nel-f.png')]

    dummy_scene = FightScene(heros)

    cocos.director.director.run(dummy_scene)

if __name__ == "__main__":
    main()
