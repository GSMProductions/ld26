# -*- coding: utf-8 -*-
import cocos

from data import TITLE, SCREEN_SIZE

def main():

    #instancification de la fenêtre
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE)

    dummy_scene = cocos.scene.Scene()

    cocos.director.director.run(dummy_scene)

if __name__ == "__main__":
    main()
