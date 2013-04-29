# -*- coding: utf-8 -*-

import cocos
import pyglet
from data import mapKey


class ImgScene(cocos.scene.Scene):

    def __init__(self,img,music=None):

        cocos.scene.Scene.__init__(self)

        layer = cocos.layer.Layer()
        image =  pyglet.image.load(img)
        sprite = cocos.sprite.Sprite(image,(0,0),anchor=(0,0))
        layer.add(sprite)
        self.add(layer)
        
        self.music =  False

        if music != None:
            self.music =  True
            self.bgm = pyglet.media.load("bgm/" + music + ".ogg", streaming=False)
            self.bgm_player = pyglet.media.Player()
            self.bgm_player.queue(self.bgm)
            self.bgm_player.eos_action = self.bgm_player.EOS_LOOP

        cocos.director.director.window.push_handlers(self)

    def on_enter(self):
        super(ImgScene, self).on_enter()
        if self.music:
            self.bgm_player.play()

    def on_exit(self):
        super(ImgScene, self).on_exit()
        if self.music:
            self.bgm_player.pause()

    def on_key_press(self,key,modifiers):
        return True

    def on_key_release(self,key,modifiers):

        key = mapKey(key)

        if key == pyglet.window.key.ESCAPE:
            cocos.director.director.window.pop_handlers()
            self.end()