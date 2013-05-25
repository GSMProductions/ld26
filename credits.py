# -*- coding: utf-8 -*-

import cocos
import pyglet
from data import mapKey


class ImgScene(cocos.scene.Scene):

    def __init__(self,img,music=None,game_over=False):

        cocos.scene.Scene.__init__(self)

        layer = cocos.layer.Layer()
        image =  pyglet.image.load(img)
        sprite = cocos.sprite.Sprite(image,(0,0),anchor=(0,0))
        layer.add(sprite)
        self.add(layer)
        
        self.music =  False
        self.game_over = game_over

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
            if self.game_over == True:
                cocos.director.director.terminate_app = True
            self.end()

class LoadingScene(ImgScene):

    def __init__(self,img,music=None,game_over=False, callback=None):
        super(LoadingScene, self).__init__(img, music, game_over)
        self.callback = callback
        pyglet.gl.glClearColor(0.85, 0.85, 0.85, 1)
        self.ready = True

        layer = cocos.layer.Layer()
        self.label = cocos.text.Label(text='Press any key',position = (400,20), font_name='Statix', color= (127,129,131,255) , font_size = 30, anchor_x = 'center')
        layer.add(self.label, z=6)
        self.add(layer, z=5)


        cocos.director.director.window.push_handlers(self)

    def on_key_press(self, key, modifiers):

        if self.ready and self.callback is not None:
            self.label.element.text = "Loading, please wait..."

    def on_key_release(self, key, modifiers):

        if self.ready and self.callback is not None:
            self.callback()
            self.label.element.text = "Have fun!"
            self.ready = False